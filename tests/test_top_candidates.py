from src.utils.data_loader import load_candidates
from src.ranking.candidate_ranker import rank_candidates

candidates = load_candidates(
    "data/candidates.jsonl"
)

results = rank_candidates(
    candidates[:5000]
)

print("\nTOP 20\n")

for candidate in results[:20]:
    print(candidate)