from src.utils.data_loader import load_candidates

from src.scoring.experience_scorer import (
    calculate_experience_score
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

candidate = candidates[0]

score = calculate_experience_score(
    candidate
)

print(
    candidate["profile"]["current_title"]
)

print(
    candidate["profile"]["years_of_experience"]
)

print(
    score
)