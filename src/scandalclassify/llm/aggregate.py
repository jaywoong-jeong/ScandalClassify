from __future__ import annotations

from collections import Counter
from typing import List, Dict

import pandas as pd


def aggregate_votes(vote_rows: List[Dict]) -> pd.DataFrame:
    by_id: Dict[int, list[str]] = {}
    for row in vote_rows:
        aid = int(row["article_id"])  # type: ignore
        label = str(row["scandal_type"])  # type: ignore
        by_id.setdefault(aid, []).append(label)

    final_rows = []
    for aid, labels in by_id.items():
        counter = Counter(labels)
        final_label, count = counter.most_common(1)[0]
        final_rows.append({"article_id": aid, "scandal_type": final_label, "vote_count": count})
    return pd.DataFrame(final_rows)


