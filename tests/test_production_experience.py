from src.utils.data_loader import load_candidates

from src.scoring.production_experience_scorer import (
    calculate_production_experience_score
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

candidate_ids = [
    "CAND_0001930",
    "CAND_0001610",
    "CAND_0003324"
]

for cid in candidate_ids:

    candidate = next(
        c for c in candidates
        if c["candidate_id"] == cid
    )

    score = (
        calculate_production_experience_score(
            candidate
        )
    )

    print(
        cid,
        candidate["profile"]["current_title"],
        score
    )