# aflvaki-example

A small Python library (`textkit`) used as a target repository for trying out the
Aflvaki orchestrator. Aflvaki clones this repository, works on a branch named
`aflvaki/<ticket>-<run id>`, and pushes that branch back here for a person to review and merge.

```bash
python -m pytest -q
```

## Functions

- `word_count(text)`: count whitespace-separated words
- `slugify(text)`: make a URL-safe identifier
