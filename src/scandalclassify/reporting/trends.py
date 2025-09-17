from __future__ import annotations

import pandas as pd


def daily_monthly_trends(df_labels: pd.DataFrame, df_source: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    # df_labels: columns [article_id, scandal_type]
    # df_source must have published_at
    src = df_source.copy()
    src["published_at"] = pd.to_datetime(src["published_at"], errors="coerce")
    merged = src.reset_index().rename(columns={"index": "article_id"}).merge(
        df_labels[["article_id", "scandal_type"]], on="article_id", how="left"
    )
    merged["scandal_type"] = merged["scandal_type"].fillna("none")

    daily = (
        merged.assign(day=merged["published_at"].dt.date)
        .groupby(["day", "scandal_type"])  # type: ignore
        .size()
        .reset_index(name="count")
        .sort_values(["day", "scandal_type"])  # type: ignore
    )

    monthly = (
        merged.assign(month=merged["published_at"].dt.to_period("M").dt.to_timestamp())
        .groupby(["month", "scandal_type"])  # type: ignore
        .size()
        .reset_index(name="count")
        .sort_values(["month", "scandal_type"])  # type: ignore
    )
    return daily, monthly


