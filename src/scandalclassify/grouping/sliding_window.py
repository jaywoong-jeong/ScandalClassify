from __future__ import annotations

from typing import List, Dict


class SlidingWindowGrouper:
    def __init__(self, total: int, window_size: int = 700, overlap_size: int = 200, min_verifications: int = 3):
        self.total = int(total)
        self.window_size = int(window_size)
        self.overlap_size = int(overlap_size)
        self.min_verifications = int(min_verifications)
        self.verification_counts = {idx: 0 for idx in range(self.total)}
        self.groups: List[list[int]] = []

    def create_base_groups(self) -> List[List[int]]:
        stride = self.window_size - self.overlap_size
        current_idx = 0
        base_groups: List[List[int]] = []
        while current_idx < self.total:
            end_idx = min(current_idx + self.window_size, self.total)
            group = list(range(current_idx, end_idx))
            if len(group) < self.window_size:
                needed = self.window_size - len(group)
                group.extend(range(needed))
            base_groups.append(group)
            current_idx += stride
            for idx in group:
                self.verification_counts[idx] += 1
        return base_groups

    def create_additional_groups(self) -> List[List[int]]:
        additional_groups: List[List[int]] = []
        while min(self.verification_counts.values()) < self.min_verifications:
            needed_articles = [idx for idx, count in self.verification_counts.items() if count < self.min_verifications]
            for i in range(0, len(needed_articles), self.window_size):
                group = needed_articles[i : i + self.window_size]
                if len(group) < self.window_size:
                    additional_needed = self.window_size - len(group)
                    group.extend(needed_articles[:additional_needed])
                additional_groups.append(group)
                for idx in group:
                    self.verification_counts[idx] += 1
        return additional_groups

    def generate_groups(self) -> List[List[int]]:
        self.groups = self.create_base_groups()
        additional = self.create_additional_groups()
        self.groups.extend(additional)
        return self.groups

    def stats(self) -> Dict[str, float]:
        counts = list(self.verification_counts.values())
        return {
            "min_verifications": min(counts) if counts else 0,
            "max_verifications": max(counts) if counts else 0,
            "avg_verifications": sum(counts) / len(counts) if counts else 0.0,
            "total_groups": len(self.groups),
        }


