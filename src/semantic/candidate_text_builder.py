def build_candidate_text(candidate):

    parts = []

    profile = candidate["profile"]

    parts.append(
        profile.get("headline", "")
    )

    parts.append(
        profile.get("summary", "")
    )

    for skill in candidate.get(
        "skills",
        []
    ):
        parts.append(
            skill["name"]
        )

    for role in candidate.get(
        "career_history",
        []
    ):
        parts.append(
            role.get(
                "description",
                ""
            )
        )

    return " ".join(parts)