# ScandalClassify

Korean news scandal classification and trend analysis using OpenAI API.

## Quickstart

Prereqs:
- Python 3.11+
- uv (Astral) installed

Setup:
1) Install dependencies
```bash
uv sync
```
2) Set your API key
```bash
export OPENAI_API_KEY=your_key_here
```
3) Run sanity check
```bash
uv run python -c "import scandalclassify; print('ScandalClassify ready')"
```

Folders:
- `src/scandalclassify/` core package modules
- `scripts/` runnable scripts (to be implemented incrementally)
- `data/` raw and processed data (gitignored)
- `notebooks/` exploration
- `configs/` configuration files

License: MIT

