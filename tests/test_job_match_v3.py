from src.utils.data_loader import (
    load_candidates
)

from src.jd.jd_parser import (
    parse_job_description
)

from src.scoring.job_match_scorer_v3 import (
    calculate_job_match_score_v3
)

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as f:

    jd_text = f.read()

jd_data = parse_job_description(
    jd_text
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

    score = (
        calculate_job_match_score_v3(
            candidate,
            jd_data
        )
    )

    print(
        cid,
        candidate["profile"][
            "current_title"
        ],
        score
    )