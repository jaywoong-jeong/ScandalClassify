from __future__ import annotations

import argparse
import json
import pandas as pd

from scandalclassify.config import load_config, ensure_dirs
from scandalclassify.llm.infer import infer_batch


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/defaults.yaml")
    parser.add_argument("--input", default="data/processed/filtered.csv")
    parser.add_argument("--groups", default="outputs/groups.json")
    parser.add_argument("--output", default="outputs/scandal_results.csv")
    args = parser.parse_args()

    cfg = load_config(args.config)
    ensure_dirs(cfg)

    df = pd.read_csv(args.input)
    with open(args.groups, "r", encoding="utf-8") as f:
        group_data = json.load(f)
    groups = group_data["groups"]

    all_rows = []
    for g in groups:
        rows = infer_batch(df, g)
        all_rows.extend(rows)

    out_df = pd.DataFrame(all_rows)
    out_df.to_csv(args.output, index=False)
    print(f"Saved results: {args.output} | rows: {len(out_df)}")


if __name__ == "__main__":
    main()


