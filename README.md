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

## Pipeline (Example)

1) Prepare data
```bash
uv run python scripts/prepare_data.py \
  --input /absolute/path/to/news_2013_q1.csv \
  --output data/processed/filtered.csv
```

2) Build groups
```bash
uv run python scripts/build_groups.py \
  --input data/processed/filtered.csv \
  --output outputs/groups.json
```

3) Run inference (requires OPENAI_API_KEY)
```bash
export OPENAI_API_KEY=your_key_here
uv run python scripts/run_infer.py \
  --input data/processed/filtered.csv \
  --groups outputs/groups.json \
  --output outputs/scandal_results.csv
```

4) Aggregate votes
```bash
uv run python scripts/aggregate_votes.py \
  --input outputs/scandal_results.csv \
  --output outputs/scandal_results_aggregated.csv
```

5) Make trends
```bash
uv run python scripts/make_trends.py \
  --labels outputs/scandal_results_aggregated.csv \
  --source data/processed/filtered.csv \
  --daily-out outputs/trends_daily.csv \
  --monthly-out outputs/trends_monthly.csv
```

