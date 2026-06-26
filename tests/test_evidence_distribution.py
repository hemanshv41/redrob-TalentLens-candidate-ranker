from src.utils.data_loader import load_candidates

from src.scoring.evidence_scorer import (
    calculate_evidence_score
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

scores = []

for candidate in candidates[:5000]:

    score = calculate_evidence_score(
        candidate
    )

    scores.append(score)

print(
    "Min:",
    min(scores)
)

print(
    "Max:",
    max(scores)
)

print(
    "Average:",
    round(
        sum(scores) / len(scores),
        2
    )
)