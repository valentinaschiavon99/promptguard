from __future__ import annotations

from functools import lru_cache

import numpy as np
from sentence_transformers import SentenceTransformer


@lru_cache(maxsize=1)
def _model(name: str) -> SentenceTransformer:
    return SentenceTransformer(name)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    a = a / (np.linalg.norm(a) + 1e-12)
    b = b / (np.linalg.norm(b) + 1e-12)
    return float(np.dot(a, b))


def semantic_similarity_score(
        prompt: str,
        output: str,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
) -> float:
    """
    Returns a similarity proxy in [0,1] (mapped from cosine [-1,1]).
    """
    m = _model(model_name)
    emb = m.encode([prompt, output], normalize_embeddings=True)
    sim = float(np.dot(emb[0], emb[1]))  # already normalized
    # cosine should be [-1,1], map to [0,1]
    return max(0.0, min(1.0, (sim + 1.0) / 2.0))