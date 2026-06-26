def calculate_experience_score(candidate):

    profile = candidate.get("profile", {})

    years = profile.get(
        "years_of_experience",
        0
    )

    current_title = profile.get(
        "current_title",
        ""
    )

    score = 0

    # Experience contribution
    score += min(years * 4, 40)

    # Seniority bonus
    senior_titles = [
        "Senior",
        "Lead",
        "Principal",
        "Architect",
        "Manager"
    ]

    if any(
        word.lower() in current_title.lower()
        for word in senior_titles
    ):
        score += 20

    return min(score, 100)