from __future__ import annotations

import argparse
import pandas as pd

from scandalclassify.llm.aggregate import aggregate_votes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/scandal_results.csv")
    parser.add_argument("--output", default="outputs/scandal_results_aggregated.csv")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    out = aggregate_votes(df.to_dict("records"))
    out.to_csv(args.output, index=False)
    print(f"Saved aggregated: {args.output} | rows: {len(out)}")


if __name__ == "__main__":
    main()


