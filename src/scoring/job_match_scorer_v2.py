AI_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "search engineer",
    "recommendation systems engineer",
    "recommendation engineer",
    "nlp engineer",
    "senior nlp engineer",
    "applied ml engineer",
    "data scientist",
    "senior data scientist",
    "computer vision engineer",
    "ai specialist",
    "senior ai engineer"
]


def calculate_job_match_score_v2(
    candidate,
    jd_data
):

    required_skills = [
        skill.lower()
        for skill in jd_data[
            "required_skills"
        ]
    ]

    # ---------------------------------
    # SKILL MATCH
    # ---------------------------------

    candidate_skills = {
        skill["name"].lower()
        for skill in candidate["skills"]
    }

    skill_matches = 0

    for skill in required_skills:

        if skill in candidate_skills:
            skill_matches += 1

    skill_score = (
        skill_matches
        /
        max(
            len(required_skills),
            1
        )
    ) * 100

    # ---------------------------------
    # EVIDENCE MATCH
    # ---------------------------------

    description_text = ""

    for role in candidate.get(
        "career_history",
        []
    ):
        description_text += " "
        description_text += role.get(
            "description",
            ""
        ).lower()

    evidence_matches = 0

    for skill in required_skills:

        if skill in description_text:
            evidence_matches += 1

    evidence_score = (
        evidence_matches
        /
        max(
            len(required_skills),
            1
        )
    ) * 100

    # ---------------------------------
    # TITLE MATCH
    # ---------------------------------

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

    for title in titles:

        if any(
            ai_title in title
            for ai_title in AI_TITLES
        ):
            title_score = 100
            break

    # ---------------------------------
    # FINAL
    # ---------------------------------

    final_score = (
        skill_score * 0.4
        + evidence_score * 0.4
        + title_score * 0.2
    )

    return round(
        final_score,
        2
    )