from src.utils.data_loader import load_candidates

from src.features.candidate_features import (
    extract_candidate_features
)

from src.scoring.technical_scorer import (
    calculate_technical_score
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

candidate = candidates[0]

features = extract_candidate_features(
    candidate
)

score = calculate_technical_score(
    features
)

print("Features:")
print(features)

print("\nTechnical Score:")
print(score)