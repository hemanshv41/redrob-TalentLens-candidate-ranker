SKILL_ALIASES = {

    "retrieval": [
        "retrieval",
        "semantic search",
        "search",
        "query expansion",
        "bm25"
    ],

    "ranking": [
        "ranking",
        "re-ranking",
        "recommendation",
        "recommendation system",
        "learning to rank"
    ],

    "embeddings": [
        "embeddings",
        "sentence-transformers",
        "vector search",
        "faiss",
        "pinecone",
        "milvus",
        "qdrant",
        "weaviate"
    ],

    "rag": [
        "rag",
        "retrieval augmented generation"
    ],

    "llms": [
        "llms",
        "prompt engineering",
        "fine-tuning llms",
        "qlora",
        "lora"
    ],

    "a/b testing": [
        "a/b testing",
        "offline metrics",
        "evaluation",
        "relevance",
        "human relevance judgments"
    ],

    "langchain": [
        "langchain",
        "llamaindex"
    ]
}


AI_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "search engineer",
    "recommendation systems engineer",
    "recommendation engineer",
    "nlp engineer",
    "applied ml engineer",
    "data scientist",
    "computer vision engineer",
    "senior ai engineer",
    "ai specialist"
]


def calculate_job_match_score_v3(
    candidate,
    jd_data
):

    required_skills = [
        skill.lower()
        for skill in jd_data[
            "required_skills"
        ]
    ]

    candidate_text = ""

    for skill in candidate["skills"]:
        candidate_text += (
            " "
            + skill["name"].lower()
        )

    for role in candidate.get(
        "career_history",
        []
    ):
        candidate_text += (
            " "
            + role.get(
                "description",
                ""
            ).lower()
        )

    # ---------------------
    # Skill/Evidence Match
    # ---------------------

    matches = 0

    for jd_skill in required_skills:

        aliases = SKILL_ALIASES.get(
            jd_skill,
            [jd_skill]
        )

        found = any(
            alias in candidate_text
            for alias in aliases
        )

        if found:
            matches += 1

    match_score = (
        matches
        /
        max(
            len(required_skills),
            1
        )
    ) * 100

    # ---------------------
    # Title Match
    # ---------------------

    title_score = 0

    titles = []

    titles.append(
        candidate["profile"][
            "current_title"
        ].lower()
    )

    for role in candidate.get(
        "career_history",
        []
    ):
        titles.append(
            role["title"].lower()
        )

    if any(
        any(
            ai_title in title
            for ai_title in AI_TITLES
        )
        for title in titles
    ):
        title_score = 100

    final_score = (
        match_score * 0.8
        + title_score * 0.2
    )

    return round(
        final_score,
        2
    )