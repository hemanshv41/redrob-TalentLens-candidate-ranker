from src.utils.data_loader import load_candidates

from src.ranking.candidate_ranker import (
    rank_candidates
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

results = rank_candidates(
    candidates[:100]
)

print("\nTOP 10\n")

for candidate in results[:10]:

    print(candidate)