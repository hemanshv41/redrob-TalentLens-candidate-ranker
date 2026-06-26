from src.utils.data_loader import load_candidates

from src.jd.jd_parser import (
    parse_job_description
)

from src.scoring.job_match_scorer import (
    calculate_job_match_score
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

for candidate in candidates[:5000]:

    score = calculate_job_match_score(
        candidate,
        jd_data
    )

    results.append(
        (
            candidate["candidate_id"],
            candidate["profile"][
                "current_title"
            ],
            score
        )
    )

results.sort(
    key=lambda x: x[2],
    reverse=True
)

for r in results[:20]:
    print(r)