# TeaserPaste Python SDK

Official Python SDK for TeaserPaste API. Simple, typed, and ready for the Teaserverse.

## Installation

```bash
# Using uv (Recommended)
uv add tp-sdk

# Using pip
pip install tp-sdk
```

## Quick Start

### Standard (Sync)

```python
import tp

# Context Manager (Recommended for connection pooling)
with tp.TeaserPaste("YOUR_API_KEY") as api:
    # Create a new paste
    note = api.paste(tp.SnippetInput(
        title="Teaserverse Logs", 
        content="System status: All green.",
        expires=tp.Expiry.HOUR_1
    ))
    print(f"Created: {note.id}")

    # Get a paste
    data = api.get(note.id)
    print(data.content)
```

### Async (AsyncIO)

```python
import asyncio
import tp

async def main():
    async with tp.AsyncTeaserPaste("YOUR_API_KEY") as api:
        note = await api.get("xyz_123")
        print(note.title)

asyncio.run(main())
```

## Features

### Connection Pooling
The SDK now supports `Context Manager` usage (using `with` statement) to reuse HTTP connections, significantly improving performance for multiple requests.

### Type Hints & Enums
Improved type safety for arguments and Models.

```python
# Use Enum for expiry
from tp import Expiry
api.paste(tp.SnippetInput(..., expires=Expiry.WEEK_1))

# Explicit arguments for edit (IDE autocompletion enabled)
api.edit(snippet_id, title="New Title", visibility="private")
```

### Iteration Helpers
Iterate through your snippets (single page only).

```python
# Iterate snippets
for snippet in api.ls_iter(include_deleted=True):
    print(snippet.title)
```

## API Reference

"One-word" API's. Both Sync and Async clients support these methods.

* `api.paste(input)` — Create a new snippet.
* `api.get(id, pwd=None)` — Get a snippet.
* `api.edit(id, title=..., ...)` — Update a snippet.
* `api.kill(id)` — Soft delete a snippet.
* `api.live(id)` — Restore a deleted snippet.
* `api.fork(id)` — Copy a snippet to your account.
* `api.star(id, on=True)` — Star (or unstar) a snippet.
* `api.ls(limit=20, include_deleted=False)` — List your snippets.
* `api.ls_iter(limit=20, include_deleted=False)` — Iterator for listing snippets (single page).
* `api.user(uid)` — List another user's public snippets.
* `api.find(q)` — Search snippets.
* `api.find_iter(q)` — Iterator for searching snippets (single page).
* `api.me()` — Get your account info.

## Configuration

You can configure the base URL via environment variable `TP_BASE_URL` or passing `base_url` to the constructor.

## Development
```bash
# Install dependencies
uv sync

# Build
uv build
```

## License

[MIT](LICENSE)
