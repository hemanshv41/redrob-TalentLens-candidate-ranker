# PRODUCTION_KEYWORDS = [
#     "production",
#     "retrieval",
#     "ranking",
#     "search",
#     "recommendation",
#     "embeddings",
#     "llm",
#     "machine learning",
#     "ml",
#     "a/b",
#     "evaluation",
#     "semantic search",
#     "vector",
#     "pipeline",
#     "deployment"
# ]


# def calculate_production_experience_score(candidate):

#     score = 0

#     history = candidate.get(
#         "career_history",
#         []
#     )

#     for role in history:

#         description = role.get(
#             "description",
#             ""
#         ).lower()

#         for keyword in PRODUCTION_KEYWORDS:

#             if keyword in description:
#                 score += 5

#     return min(score, 100)

EVIDENCE_KEYWORDS = {
    "semantic search": 15,
    "sentence-transformers": 15,
    "faiss": 15,
    "recommendation": 12,
    "ranking": 12,
    "a/b testing": 10,
    "embeddings": 10,
    "retrieval": 10,
    "query expansion": 10,
    "lightgbm": 8,
    "xgboost": 8,
    "bm25": 8,
    "relevance": 8,
    "vector": 8,
    "fine-tuning": 8,
    "llm": 8,
    "kafka": 5,
    "spark": 5,
    "pyspark": 5,
    "airflow": 5,
    "data pipeline": 8,
    "feature pipeline": 10,
    "feature engineering": 8,
    "streaming": 5,
    "real-time": 5,
}


def calculate_production_experience_score(candidate):

    score = 0

    history = candidate.get(
        "career_history",
        []
    )

    for role in history:

        description = role.get(
            "description",
            ""
        ).lower()

        for keyword, weight in (
            EVIDENCE_KEYWORDS.items()
        ):

            if keyword in description:
                score += weight

    return min(score, 100)