from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def load_pairs_csv(
        path: str | Path,
        prompt_col: str = "prompt",
        output_col: str = "output",
        limit: int = 0,
) -> list[dict]:
    """
    Load prompt/output pairs from a CSV.

    Returns: [{"prompt": "...", "output": "..."}]
    """
    df = pd.read_csv(path)

    # fallback: try common alternative column names
    if prompt_col not in df.columns:
        for c in ["instruction", "input", "question", "user_prompt"]:
            if c in df.columns:
                prompt_col = c
                break

    if output_col not in df.columns:
        for c in ["response", "answer", "completion", "model_output"]:
            if c in df.columns:
                output_col = c
                break

    if prompt_col not in df.columns or output_col not in df.columns:
        raise ValueError(
            f"CSV must contain columns for prompt/output. Found: {list(df.columns)}"
        )

    if limit and limit > 0:
        df = df.head(limit)

    pairs: list[dict] = []
    for _, r in df.iterrows():
        pairs.append(
            {
                "prompt": str(r[prompt_col]) if pd.notna(r[prompt_col]) else "",
                "output": str(r[output_col]) if pd.notna(r[output_col]) else "",
            }
        )
    return pairs