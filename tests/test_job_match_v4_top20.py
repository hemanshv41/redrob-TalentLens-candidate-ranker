from src.utils.data_loader import (
    load_candidates
)

from src.jd.jd_parser import (
    parse_job_description
)

from src.scoring.job_match_scorer_v4 import (
    calculate_job_match_score_v4
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

results = []

for candidate in candidates:

    score = (
        calculate_job_match_score_v4(
            candidate,
            jd_data
        )
    )

    results.append(
        (
            candidate["candidate_id"],
            candidate["profile"]["current_title"],
            score
        )
    )

results.sort(
    key=lambda x: x[2],
    reverse=True
)

print("\nTOP 20 JD MATCHES\n")

for r in results[:20]:
    print(r)