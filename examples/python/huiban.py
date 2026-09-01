"""Minimal Conference Partner API client — standard library only, no dependencies.

Set HUIBAN_API_KEY to use your account quota (200/day) instead of the anonymous
per-IP one (50/day). Search, ranking lists and statistics work without a key.
Get a key at https://www.myhuiban.com/account/api-keys
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ.get("HUIBAN_BASE_URL", "https://www.myhuiban.com")
UA = "conference-partner-example/1.0 (+https://github.com/sundou82/conference-partner-mcp)"

#: Worth trying again. The API is behind Cloudflare, so a momentary origin stall
#: arrives as 520-524 rather than a plain 5xx. 401/402/429 are deliberately absent:
#: they will not heal on their own, and their message says what to do instead.
TRANSIENT = {500, 502, 503, 504, 520, 521, 522, 523, 524}

FIELDS = ["ai", "vision", "nlp", "data", "network", "security", "se",
          "systems", "theory", "hci", "graphics", "bio", "robotics", "web"]

#: Quota headroom reported by the last response, or None if the server sent no header.
quota_remaining = None


class ApiError(RuntimeError):
    pass


def _open(request, attempts=3):
    """urlopen, retrying the errors that clear up by themselves.

    HTTPError subclasses URLError, so the narrower clause has to come first.
    """
    for attempt in range(1, attempts + 1):
        try:
            return urllib.request.urlopen(request, timeout=30)
        except urllib.error.HTTPError as error:
            if error.code not in TRANSIENT or attempt == attempts:
                raise
        except urllib.error.URLError:            # connection reset, DNS, timeout
            if attempt == attempts:
                raise
        time.sleep(2 ** attempt)


def _reason(error):
    """The server's own message, or the reason phrase when the body is not ours.

    Not every error body is JSON. An edge rule, a WAF or an origin error page
    answers in HTML or plain text, and `json.loads` then raises JSONDecodeError
    from inside the handler — which loses the status code, the single most
    useful thing we had. That is not hypothetical: on 2026-08-31 an over-broad
    edge rule started answering `?page=1&per_page=100` with `410 Gone` and a
    two-word body, and this client reported it as
    `Expecting value: line 1 column 1 (char 0)`.
    """
    try:
        body = error.read() or b""
    except OSError:                          # connection died mid-body
        return error.reason

    try:
        payload = json.loads(body)
        message = payload.get("message") if isinstance(payload, dict) else None
    except ValueError:
        # Not our envelope. A short plain-text body ("Gone") is worth repeating;
        # a whole HTML error page is not — the status line already says more than
        # its first tag does.
        text = body.decode("utf-8", "replace").strip()
        message = text if text and "<" not in text and len(text) <= 200 else None

    return message or error.reason


def get(path, params=None):
    """GET an endpoint and return its `data` payload.

    Raises ApiError with the server's own message, which for 401/402/429 explains
    exactly what to do next.
    """
    global quota_remaining

    query = urllib.parse.urlencode(
        {k: v for k, v in (params or {}).items() if v not in (None, "")}
    )
    url = f"{BASE}{path}" + (f"?{query}" if query else "")

    request = urllib.request.Request(url)
    request.add_header("Accept", "application/json")
    # A real User-Agent matters: the default `Python-urllib/3.x` is turned away at the edge.
    request.add_header("User-Agent", UA)

    key = os.environ.get("HUIBAN_API_KEY")
    if key:
        request.add_header("Authorization", f"Bearer {key}")

    try:
        with _open(request) as response:
            quota_remaining = response.headers.get("X-Quota-Remaining")
            body = json.loads(response.read())
    except urllib.error.HTTPError as error:
        raise ApiError(f"HTTP {error.code}: {_reason(error)}") from None

    # Validation problems come back as HTTP 200 with a non-200 code in the envelope.
    if body.get("code") != 200:
        raise ApiError(f"API error {body['code']}: {body.get('message')}")

    return body["data"]


def paginate(path, params, key, per_page=100, max_pages=20):
    """Yield every row across pages. `key` is 'conferences' or 'journals'.

    Handles both pagination shapes the API uses: search endpoints report
    {total, total_pages}, ranking-list endpoints report {count, has_more}.

    max_pages is a guard, not a limit of the API — each page costs one request
    against your daily quota, so a runaway filter should not spend all of it.
    """
    page = 1
    while page <= max_pages:
        data = get(path, {**params, "page": page, "per_page": per_page})
        yield from data[key]

        pagination = data["pagination"]
        if "total_pages" in pagination:
            if page >= pagination["total_pages"]:
                return
        elif not pagination.get("has_more"):
            return
        page += 1

    print(f"warning: stopped at {max_pages} pages; narrow the filter or raise max_pages",
          file=sys.stderr)
