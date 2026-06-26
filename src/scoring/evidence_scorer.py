# EVIDENCE_TERMS = [
#     "built",
#     "implemented",
#     "developed",
#     "designed",
#     "created",
#     "deployed",
#     "shipped",
#     "launched",
#     "production",
#     "improved",
#     "optimized",
#     "owned"
# ]

# AI_TERMS = [
#     "retrieval",
#     "ranking",
#     "recommendation",
#     "semantic search",
#     "faiss",
#     "sentence-transformers",
#     "embeddings",
#     "rag",
#     "llm",
#     "langchain",
#     "vector",
#     "a/b testing",
#     "query expansion"
# ]


# def calculate_evidence_score(candidate):

#     text = ""

#     for role in candidate.get(
#         "career_history",
#         []
#     ):
#         text += " "
#         text += role.get(
#             "description",
#             ""
#         ).lower()

#     score = 0

#     for evidence in EVIDENCE_TERMS:

#         if evidence in text:

#             for ai_term in AI_TERMS:

#                 if ai_term in text:

#                     score += 5

#     return min(score, 100)

RETRIEVAL_TERMS = [
    "semantic search",
    "retrieval",
    "query expansion",
    "bm25",
    "faiss"
]

RANKING_TERMS = [
    "ranking",
    "re-ranking",
    "recommendation",
    "recommendation system"
]

EMBEDDING_TERMS = [
    "embeddings",
    "sentence-transformers",
    "vector",
    "vector search"
]

EXPERIMENT_TERMS = [
    "a/b testing",
    "offline metrics",
    "relevance",
    "evaluation",
    "human relevance judgments"
]

PRODUCTION_TERMS = [
    "production",
    "deployed",
    "launched",
    "shipping",
    "users",
    "served",
    "serving"
]


def calculate_evidence_score(candidate):

    text = ""

    for role in candidate.get(
        "career_history",
        []
    ):
        text += " "
        text += role.get(
            "description",
            ""
        ).lower()

    score = 0

    # Retrieval
    if any(
        term in text
        for term in RETRIEVAL_TERMS
    ):
        score += 20

    # Ranking
    if any(
        term in text
        for term in RANKING_TERMS
    ):
        score += 20

    # Embeddings
    if any(
        term in text
        for term in EMBEDDING_TERMS
    ):
        score += 20

    # Experimentation
    if any(
        term in text
        for term in EXPERIMENT_TERMS
    ):
        score += 20

    # Production
    if any(
        term in text
        for term in PRODUCTION_TERMS
    ):
        score += 20

    return score