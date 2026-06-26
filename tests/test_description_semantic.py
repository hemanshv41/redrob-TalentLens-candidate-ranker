from src.utils.data_loader import (
    load_candidates
)

from src.semantic.semantic_matcher import (
    semantic_similarity
)

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as f:

    jd = f.read()

candidates = load_candidates(
    "data/candidates.jsonl"
)

candidate_ids = [
    "CAND_0001610",
    "CAND_0001930",
    "CAND_0003324"
]

for cid in candidate_ids:

    candidate = next(
        c for c in candidates
        if c["candidate_id"] == cid
    )

    descriptions = []

    for role in candidate["career_history"]:
        descriptions.append(
            role["description"]
        )

    text = " ".join(descriptions)

    score = semantic_similarity(
        jd,
        text
    )

    print(
        cid,
        candidate["profile"]["current_title"],
        score
    )