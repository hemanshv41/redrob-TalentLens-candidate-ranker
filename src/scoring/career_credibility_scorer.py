AI_ROLE_KEYWORDS = [
    "machine learning",
    "ml",
    "data scientist",
    "ai engineer",
    "computer vision",
    "nlp",
    "recommendation",
    "search",
    "retrieval",
    "data engineer",
    "analytics engineer",
    "backend engineer",
    "software engineer",
]


def calculate_career_credibility_score(candidate):

    history = candidate.get(
        "career_history",
        []
    )

    score = 0

    for role in history:

        title = role.get(
            "title",
            ""
        ).lower()

        for keyword in AI_ROLE_KEYWORDS:

            if keyword in title:
                score += 25
                break

    return min(score, 100)