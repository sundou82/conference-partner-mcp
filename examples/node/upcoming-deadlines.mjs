#!/usr/bin/env node
// List conference submission deadlines coming up in the next N days.
// No dependencies, no API key needed — search is part of the anonymous tier.
//
//   node upcoming-deadlines.mjs --days 90 --field ai --ccf A
//   node upcoming-deadlines.mjs --days 30 --query neural --json
//
// Set HUIBAN_API_KEY to draw on your account quota (200/day) instead of the
// anonymous per-IP one (50/day): https://www.myhuiban.com/account/api-keys

const BASE = process.env.HUIBAN_BASE_URL ?? 'https://www.myhuiban.com';
const UA = 'conference-partner-example/1.0 (+https://github.com/sundou82/conference-partner-mcp)';

const args = Object.fromEntries(
  process.argv.slice(2).flatMap((token, i, all) =>
    token.startsWith('--')
      ? [[token.slice(2), all[i + 1]?.startsWith('--') ?? true ? true : all[i + 1]]]
      : []
  )
);

let quotaRemaining = null;

async function get(path, params) {
  const query = new URLSearchParams(
    Object.entries(params).filter(([, v]) => v !== undefined && v !== null && v !== '')
  );

  const headers = { Accept: 'application/json', 'User-Agent': UA };
  if (process.env.HUIBAN_API_KEY) {
    headers.Authorization = `Bearer ${process.env.HUIBAN_API_KEY}`;
  }

  const response = await fetch(`${BASE}${path}?${query}`, { headers });
  quotaRemaining = response.headers.get('x-quota-remaining');
  const body = await response.json().catch(() => ({}));

  // 401/402/429 all carry a message saying exactly what to do next.
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${body.message ?? response.statusText}`);
  // Validation problems arrive as HTTP 200 with a non-200 code in the envelope.
  if (body.code !== 200) throw new Error(`API error ${body.code}: ${body.message}`);

  return body.data;
}

// Handles both pagination shapes: search reports {total, total_pages},
// ranking lists report {count, has_more}.
async function* paginate(path, params, key, perPage = 100, maxPages = 20) {
  for (let page = 1; page <= maxPages; page++) {
    const data = await get(path, { ...params, page, per_page: perPage });
    yield* data[key];
    const { total_pages: totalPages, has_more: hasMore } = data.pagination;
    if (totalPages !== undefined ? page >= totalPages : !hasMore) return;
  }
  console.error(`warning: stopped at ${maxPages} pages; narrow the filter`);
}

const days = Number(args.days ?? 90);
const today = new Date();
const until = new Date(today.getTime() + days * 86400_000);
const iso = (d) => d.toISOString().slice(0, 10);

const rows = [];
try {
  for await (const row of paginate('/api/conferences', {
    query: args.query,
    field: args.field,
    ccf_rank: args.ccf,
    core_rank: args.core,
    submission_date_start: iso(today),
    submission_date_end: iso(until),
  }, 'conferences')) {
    rows.push(row);
  }
} catch (error) {
  console.error(error.message);
  process.exit(1);
}

rows.sort((a, b) => (a.submission_date ?? '').localeCompare(b.submission_date ?? ''));

if (args.json) {
  console.log(JSON.stringify(rows, null, 2));
} else if (rows.length === 0) {
  console.log(`Nothing due in the next ${days} days for that filter.`);
} else {
  console.log(`${rows.length} deadlines in the next ${days} days\n`);
  for (const row of rows) {
    const left = Math.round((Date.parse(row.submission_date) - today) / 86400_000);
    const ranks = [row.ccf_rank, row.core_rank].filter(Boolean).join('/') || '-';
    const extended = row.is_extended ? '  (extended)' : '';
    console.log(
      `${row.submission_date}  ${String(left).padStart(4)}d  ` +
      `${row.short_name.padEnd(14)} ${ranks.padEnd(8)} ${row.full_name.slice(0, 56)}${extended}`
    );
  }
  if (quotaRemaining) console.log(`\nQuota remaining today: ${quotaRemaining}`);
}
