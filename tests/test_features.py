from src.utils.data_loader import load_candidates
from src.features.candidate_features import (
    extract_candidate_features
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

features = extract_candidate_features(
    candidates[0]
)

print(features)