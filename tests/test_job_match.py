from src.utils.data_loader import load_candidates

from src.jd.jd_parser import (
    parse_job_description
)

from src.scoring.job_match_scorer import (
    calculate_job_match_score
)

jd = """
Looking for an AI Engineer with experience in:

NLP
RAG
LLMs
Sentence Transformers
FAISS
Embeddings
"""

jd_data = parse_job_description(jd)

candidates = load_candidates(
    "data/candidates.jsonl"
)

candidate = candidates[0]

score = calculate_job_match_score(
    candidate,
    jd_data
)

print(
    candidate["candidate_id"]
)

print(score)