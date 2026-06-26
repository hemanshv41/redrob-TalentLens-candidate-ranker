from src.utils.data_loader import load_candidates

from src.ranking.candidate_ranker import (
    rank_candidate
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

results = []

for candidate in candidates[:5000]:

    results.append(
        rank_candidate(candidate)
    )

results = sorted(
    results,
    key=lambda x: x["final_score"],
    reverse=True
)

print("\nTOP 20 CANDIDATES\n")

for r in results[:20]:
    print(r)