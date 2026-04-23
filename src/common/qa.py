from typing import Any, Dict

import pandas as pd


def check_missing_props(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_rows": len(df),
        "missing_counts": df.isnull().sum().to_dict(),
        "missing_pct": (df.isnull().mean() * 100).round(2).to_dict(),
    }


def check_duplicate_rows(df: pd.DataFrame, subset: list = None) -> Dict[str, Any]:
    dupes = df.duplicated(subset=subset)
    return {
        "total_rows": len(df),
        "duplicate_rows": int(dupes.sum()),
        "duplicate_pct": round(dupes.mean() * 100, 2),
    }
