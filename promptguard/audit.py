from __future__ import annotations

from promptguard.checks import formal_flags, rule_conformity_score
from promptguard.embeddings import semantic_similarity_score


def audit_one(prompt: str, output: str) -> dict:
    flags = formal_flags(output)
    rule = rule_conformity_score(prompt, output)
    sem = semantic_similarity_score(prompt, output)

    # Simple risk composition (tunable weights)
    risk = 0.0
    risk += 0.45 * (1.0 - sem)
    risk += 0.35 * (1.0 - rule)
    risk += 0.20 * min(1.0, len(flags) / 5.0)
    risk = max(0.0, min(1.0, risk))

    return {
        "prompt": prompt,
        "output": output,
        "scores": {
            "semantic_similarity": round(sem, 4),
            "rule_conformity": round(rule, 4),
            "risk": round(risk, 4),
        },
        "flags": flags,
    }


def audit_pairs(pairs: list[dict]) -> dict:
    items = [audit_one(p["prompt"], p["output"]) for p in pairs]
    return {"items": items, "count": len(items)}