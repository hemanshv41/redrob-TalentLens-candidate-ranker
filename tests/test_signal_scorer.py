from src.utils.data_loader import load_candidates

from src.scoring.signal_scorer import (
    calculate_signal_score
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

candidate = candidates[0]

signals = candidate["redrob_signals"]

score = calculate_signal_score(
    signals
)

print("Signal Score")
print(score)
print(signals)