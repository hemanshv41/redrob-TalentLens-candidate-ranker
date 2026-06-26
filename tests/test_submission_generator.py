# from src.ranking.candidate_ranker import (
#     rank_candidates
# )

# from src.utils.data_loader import (
#     load_candidates
# )

# from src.output.submission_generator import (
#     save_submission
# )

# candidates = load_candidates(
#     "data/candidates.jsonl"
# )

# ranked = rank_candidates(
#     candidates[:1000]
# )

# save_submission(
#     ranked,
#     "submission.csv"
# )

from src.ranking.candidate_ranker import (
    rank_candidates
)

from src.utils.data_loader import (
    load_candidates
)

from src.output.submission_generator import (
    save_submission
)

from src.jd.jd_parser import (
    parse_job_description
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

ranked = rank_candidates(
    candidates,
    jd_data
)

save_submission(
    ranked,
    
    "submission.csv"
)