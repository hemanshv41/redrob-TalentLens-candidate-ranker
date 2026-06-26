from src.utils.data_loader import load_candidates
import json

candidates = load_candidates(
    "data/candidates.jsonl"
)

with open(
    "data/demo_candidates.jsonl",
    "w",
    encoding="utf-8"
) as f:

    for candidate in candidates[:500]:

        f.write(
            json.dumps(candidate)
            + "\n"
        )

print(
    "Created demo dataset."
)