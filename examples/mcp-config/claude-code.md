# Claude Code

Anonymous (search, ranking lists, statistics):

    claude mcp add --transport http conference-partner https://www.myhuiban.com/mcp

With a key, unlocking the detail tools:

    claude mcp add --transport http conference-partner https://www.myhuiban.com/mcp \
      --header "Authorization: Bearer hb_YOUR_KEY"

Or commit `.mcp.json` at the project root — see `claude-code.mcp.json` in this directory.
