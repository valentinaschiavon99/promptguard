from __future__ import annotations

import re


_AI_DISCLAIMER_PATTERNS = [
    r"\bas an ai\b",
    r"\bas a language model\b",
    r"\bi can't\b",
    r"\bi cannot\b",
]

def formal_flags(output: str) -> list[str]:
    flags: list[str] = []
    text = (output or "").strip()

    if not text:
        flags.append("empty_output")
        return flags

    if len(text) < 10:
        flags.append("too_short")

    if "lorem ipsum" in text.lower():
        flags.append("placeholder_text")

    for pat in _AI_DISCLAIMER_PATTERNS:
        if re.search(pat, text.lower()):
            flags.append("ai_disclaimer")

    if text.count("```") >= 2:
        flags.append("contains_code_block")

    return sorted(set(flags))


def rule_conformity_score(prompt: str, output: str) -> float:
    """
    Lightweight heuristic score in [0,1].
    Not 'truth' — just a simple proxy for quality & formatting.
    """
    flags = formal_flags(output)
    score = 1.0

    # penalize based on flags
    penalties = {
        "empty_output": 1.0,
        "too_short": 0.3,
        "placeholder_text": 0.4,
        "ai_disclaimer": 0.2,
        "contains_code_block": 0.1,
    }
    for f in flags:
        score -= penalties.get(f, 0.1)

    return max(0.0, min(1.0, score))