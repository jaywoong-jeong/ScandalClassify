from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import yaml


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_config(config_path: str | Path = "configs/defaults.yaml") -> Dict[str, Any]:
    path = Path(config_path)
    if not path.is_absolute():
        path = project_root() / path
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data


def ensure_dirs(cfg: Dict[str, Any]) -> None:
    paths = cfg.get("paths", {})
    for key in [
        "data_root",
        "raw_dir",
        "processed_dir",
        "outputs_dir",
        "artifacts_dir",
        "logs_dir",
    ]:
        if key in paths:
            Path(paths[key]).mkdir(parents=True, exist_ok=True)


