from src.utils.data_loader import (
    load_candidates
)

from src.scoring.evidence_scorer import (
    calculate_evidence_score
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

for cid in [
    "CAND_0001610",
    "CAND_0001930",
    "CAND_0003324"
]:

    candidate = next(
        c for c in candidates
        if c["candidate_id"] == cid
    )

    print(
        cid,
        candidate["profile"]["current_title"],
        calculate_evidence_score(
            candidate
        )
    )