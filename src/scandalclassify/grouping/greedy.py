from __future__ import annotations

from typing import List, Tuple


def greedy_assignment(n: int, k: int, l: int) -> Tuple[List[list[int]], list[int]]:
    verification_count = [0] * n
    batches: List[list[int]] = []
    while any(v < k for v in verification_count):
        current_batch: list[int] = []
        for i in sorted(range(n), key=lambda x: verification_count[x]):
            if verification_count[i] < k and i not in current_batch:
                current_batch.append(i)
                if len(current_batch) >= l:
                    break
        if not current_batch:
            break
        batches.append(current_batch)
        for i in current_batch:
            verification_count[i] += 1
    return batches, verification_count


