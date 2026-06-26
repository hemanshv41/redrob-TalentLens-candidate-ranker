from src.utils.data_loader import (
    load_candidates
)

from src.semantic.candidate_text_builder import (
    build_candidate_text
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

candidate = next(
    c for c in candidates
    if c["candidate_id"] == "CAND_0001610"
)

text = build_candidate_text(
    candidate
)

score = semantic_similarity(
    jd,
    text
)

print(score)