def generate_explanation(result):

    reasons = []

    if result["ai_score"] >= 80:
        reasons.append(
            "Strong AI and machine learning expertise"
        )

    if result["career_credibility"] >= 50:
        reasons.append(
            "Relevant AI-focused career history"
        )

    if result["production_experience_score"] >= 50:
        reasons.append(
            "Demonstrated production ML and retrieval system experience"
        )

    if result["signal_score"] >= 60:
        reasons.append(
            "Strong recruiter and platform engagement signals"
        )

    return reasons