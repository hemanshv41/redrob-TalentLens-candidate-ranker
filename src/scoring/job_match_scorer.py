def calculate_job_match_score(
    candidate,
    jd_data
):

    candidate_skills = {
        skill["name"]
        for skill in candidate["skills"]
    }

    required_skills = set(
        jd_data["required_skills"]
    )

    matches = (
        candidate_skills
        &
        required_skills
    )

    if not required_skills:
        return 0

    return round(
        len(matches)
        /
        len(required_skills)
        *
        100,
        2
    )