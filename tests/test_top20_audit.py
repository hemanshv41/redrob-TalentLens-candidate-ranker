from src.utils.data_loader import load_candidates
from src.ranking.candidate_ranker import rank_candidates

candidates = load_candidates(
    "data/candidates.jsonl"
)

results = rank_candidates(
    candidates
)

for result in results[:20]:

    cid = result["candidate_id"]

    candidate = next(
        c for c in candidates
        if c["candidate_id"] == cid
    )

    print("\n" + "=" * 100)

    print(
        cid,
        candidate["profile"]["current_title"]
    )

    print(
        "FINAL SCORE:",
        result["final_score"]
    )

    print("\nCAREER HISTORY")

    for role in candidate[
        "career_history"
    ]:

        print(
            "-",
            role["title"]
        )

    print("\nTOP SKILLS")

    for skill in candidate[
        "skills"
    ][:10]:

        print(
            "-",
            skill["name"]
        )