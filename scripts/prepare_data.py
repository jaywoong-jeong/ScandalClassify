from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

from scandalclassify.config import load_config, ensure_dirs
from scandalclassify.data.loader import load_csv, filter_by_date
from scandalclassify.data.preprocess import basic_clean


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/defaults.yaml")
    parser.add_argument("--input", default=None)
    parser.add_argument("--output", default="data/processed/filtered.csv")
    args = parser.parse_args()

    cfg = load_config(args.config)
    ensure_dirs(cfg)

    source_csv = args.input or cfg.get("input", {}).get("source_csv", "")
    if not source_csv:
        raise SystemExit("No input CSV provided. Use --input or set input.source_csv in config.")

    df = load_csv(source_csv)
    date_cfg = cfg.get("input", {}).get("date_filter", {})
    df = filter_by_date(
        df,
        start=date_cfg.get("start"),
        end=date_cfg.get("end"),
        months=date_cfg.get("months"),
    )

    pre_cfg = cfg.get("preprocess", {})
    df = basic_clean(
        df,
        drop_null=pre_cfg.get("drop_null", True),
        deduplicate_on=pre_cfg.get("deduplicate_on", None),
        min_content_chars=pre_cfg.get("min_content_chars", 0),
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Saved processed CSV: {out_path}")


if __name__ == "__main__":
    main()


