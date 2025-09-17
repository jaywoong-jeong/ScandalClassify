from __future__ import annotations

import argparse
import pandas as pd

from scandalclassify.reporting.trends import daily_monthly_trends


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--labels", default="outputs/scandal_results_aggregated.csv")
    parser.add_argument("--source", default="data/processed/filtered.csv")
    parser.add_argument("--daily-out", default="outputs/trends_daily.csv")
    parser.add_argument("--monthly-out", default="outputs/trends_monthly.csv")
    args = parser.parse_args()

    labels = pd.read_csv(args.labels)
    src = pd.read_csv(args.source)
    daily, monthly = daily_monthly_trends(labels, src)
    daily.to_csv(args.daily_out, index=False)
    monthly.to_csv(args.monthly_out, index=False)
    print(f"Saved trends: {args.daily_out}, {args.monthly_out}")


if __name__ == "__main__":
    main()


