# def generate_explanation(result):

#     reasons = []

#     if result["ai_score"] >= 80:
#         reasons.append(
#             "Strong AI and machine learning expertise"
#         )

#     if result["career_credibility"] >= 50:
#         reasons.append(
#             "Relevant AI-focused career history"
#         )

#     if result["production_experience_score"] >= 50:
#         reasons.append(
#             "Demonstrated production ML and retrieval system experience"
#         )

#     if result["signal_score"] >= 60:
#         reasons.append(
#             "Strong recruiter and platform engagement signals"
#         )

#     return ". ".join(reasons)


# def generate_explanation(result):

#     title = result["title"]

#     reasons = []

#     reasons.append(
#         f"{title} with strong AI and machine learning background"
#     )

#     if result["job_match_score"] >= 70:

#         reasons.append(
#             "Strong alignment with retrieval, ranking and search requirements"
#         )

#     elif result["job_match_score"] >= 50:

#         reasons.append(
#             "Good alignment with key JD requirements"
#         )

#     if result["production_experience_score"] >= 75:

#         reasons.append(
#             "Demonstrated production search and retrieval system experience"
#         )

#     elif result["production_experience_score"] >= 50:

#         reasons.append(
#             "Evidence of production ML deployment experience"
#         )

#     if result["evidence_score"] >= 80:

#         reasons.append(
#             "Profile contains strong technical evidence beyond keyword matching"
#         )

#     elif result["evidence_score"] >= 40:

#         reasons.append(
#             "Profile contains relevant technical project evidence"
#         )

#     return ". ".join(reasons) + "."

def generate_explanation(result):

    title = result["title"]

    reasons = []

    # Primary reason varies by strongest signal

    if result["job_match_score"] >= 75:

        reasons.append(
            f"{title} with exceptional alignment to retrieval, ranking and search requirements"
        )

    elif result["production_experience_score"] >= 75:

        reasons.append(
            f"{title} with strong production search and ML deployment experience"
        )

    elif result["evidence_score"] >= 80:

        reasons.append(
            f"{title} with substantial technical evidence and applied AI experience"
        )

    else:

        reasons.append(
            f"{title} with relevant AI and machine learning background"
        )

    # JD Match

    if result["job_match_score"] >= 70:

        reasons.append(
            "Strong alignment with retrieval, ranking and search requirements"
        )

    elif result["job_match_score"] >= 50:

        reasons.append(
            "Good alignment with key job description requirements"
        )

    # Production Experience

    if result["production_experience_score"] >= 75:

        reasons.append(
            "Demonstrated production search and retrieval system experience"
        )

    elif result["production_experience_score"] >= 50:

        reasons.append(
            "Evidence of production ML deployment experience"
        )

    # Evidence Score

    if result["evidence_score"] >= 80:

        reasons.append(
            "Profile contains strong technical evidence beyond keyword matching"
        )

    elif result["evidence_score"] >= 40:

        reasons.append(
            "Profile contains relevant technical project evidence"
        )

    # Career credibility

    if result["career_credibility"] >= 75:

        reasons.append(
            "Consistent AI-focused career progression"
        )

    # Signal strength

    if result["signal_score"] >= 75:

        reasons.append(
            "Strong recruiter and platform engagement signals"
        )

    return ". ".join(reasons) + "."