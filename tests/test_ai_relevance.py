from src.utils.data_loader import load_candidates

from src.scoring.ai_relevance_scorer import (
    calculate_ai_relevance_score
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

candidate = candidates[0]

score = calculate_ai_relevance_score(
    candidate
)

print(
    candidate["profile"]["current_title"]
)

print(score)