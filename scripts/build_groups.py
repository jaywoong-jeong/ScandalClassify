from __future__ import annotations

import argparse
import json
import pandas as pd

from scandalclassify.config import load_config, ensure_dirs
from scandalclassify.grouping.sliding_window import SlidingWindowGrouper


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/defaults.yaml")
    parser.add_argument("--input", default="data/processed/filtered.csv")
    parser.add_argument("--output", default="outputs/groups.json")
    args = parser.parse_args()

    cfg = load_config(args.config)
    ensure_dirs(cfg)

    df = pd.read_csv(args.input)
    gcfg = cfg.get("grouping", {})
    grouper = SlidingWindowGrouper(
        total=len(df),
        window_size=gcfg.get("window_size", 700),
        overlap_size=gcfg.get("overlap_size", 200),
        min_verifications=gcfg.get("min_verifications", 3),
    )
    groups = grouper.generate_groups()
    stats = grouper.stats()

    out = {"groups": groups, "stats": stats}
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print(f"Saved groups: {args.output} | stats: {stats}")


if __name__ == "__main__":
    main()


