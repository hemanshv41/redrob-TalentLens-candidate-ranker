from src.scoring.job_match_scorer_v3 import (
    SKILL_ALIASES,
    AI_TITLES
)


def calculate_job_match_score_v4(
    candidate,
    jd_data
):

    required_skills = [
        skill.lower()
        for skill in jd_data[
            "required_skills"
        ]
    ]

    # ---------------------
    # SKILLS TEXT
    # ---------------------

    skills_text = " ".join(
        skill["name"].lower()
        for skill in candidate["skills"]
    )

    # ---------------------
    # DESCRIPTION TEXT
    # ---------------------

    description_text = ""

    for role in candidate.get(
        "career_history",
        []
    ):
        description_text += (
            " "
            + role.get(
                "description",
                ""
            ).lower()
        )

    # ---------------------
    # SKILL SCORE
    # ---------------------

    skill_matches = 0

    for jd_skill in required_skills:

        aliases = SKILL_ALIASES.get(
            jd_skill,
            [jd_skill]
        )

        if any(
            alias in skills_text
            for alias in aliases
        ):
            skill_matches += 1

    skill_score = (
        skill_matches
        /
        max(
            len(required_skills),
            1
        )
    ) * 100

    # ---------------------
    # DESCRIPTION SCORE
    # ---------------------

    description_matches = 0

    for jd_skill in required_skills:

        aliases = SKILL_ALIASES.get(
            jd_skill,
            [jd_skill]
        )

        if any(
            alias in description_text
            for alias in aliases
        ):
            description_matches += 1

    description_score = (
        description_matches
        /
        max(
            len(required_skills),
            1
        )
    ) * 100

    # ---------------------
    # TITLE SCORE
    # ---------------------

    title_score = 0

    titles = [
        candidate["profile"][
            "current_title"
        ].lower()
    ]

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

    # ---------------------
    # FINAL
    # ---------------------

    final_score = (
        skill_score * 0.20
        + description_score * 0.70
        + title_score * 0.10
    )

    return round(
        final_score,
        2
    )