AI_RELATED_KEYWORDS = [
    "machine learning",
    "ml",
    "ai",
    "artificial intelligence",
    "data scientist",
    "data engineer",
    "analytics",
    "backend",
    "software engineer",
    "computer vision",
    "nlp",
    "recommendation",
    "search",
    "retrieval"
]


def calculate_career_affinity_score(candidate):

    score = 0

    history = candidate.get(
        "career_history",
        []
    )

    for job in history:

        title = job.get(
            "title",
            ""
        ).lower()

        for keyword in AI_RELATED_KEYWORDS:

            if keyword in title:
                score += 20
                break

    return min(score, 100)