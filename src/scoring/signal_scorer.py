# def calculate_signal_score(signals):

#     score = 0

#     score += signals.get(
#         "github_activity_score", 0
#     ) * 2

#     score += signals.get(
#         "recruiter_response_rate", 0
#     ) * 20

#     score += signals.get(
#         "interview_completion_rate", 0
#     ) * 20

#     score += signals.get(
#         "profile_completeness_score", 0
#     ) * 10

#     score += min(
#         signals.get(
#             "saved_by_recruiters_30d", 0
#         ) / 2,
#         10
#     )

#     score += min(
#         signals.get(
#             "search_appearance_30d", 0
#         ) / 10,
#         10
#     )

#     return min(round(score, 2), 100)


def calculate_signal_score(signals):

    score = 0

    # 0-20
    score += (
        signals.get(
            "profile_completeness_score",
            0
        ) / 100
    ) * 20

    # 0-20
    github_score = max(
        0,
        signals.get(
            "github_activity_score",
            0
        )
    )

    score += min(
        github_score,
        10
    ) * 2

    # 0-15
    score += (
        signals.get(
            "recruiter_response_rate",
            0
        )
    ) * 15

    # 0-15
    score += (
        signals.get(
            "interview_completion_rate",
            0
        )
    ) * 15

    # 0-10
    score += min(
        signals.get(
            "saved_by_recruiters_30d",
            0
        ),
        10
    )

    # 0-10
    score += min(
        signals.get(
            "search_appearance_30d",
            0
        ) / 100,
        10
    )

    # Verification bonus
    if signals.get("verified_email"):
        score += 3

    if signals.get("verified_phone"):
        score += 3

    if signals.get("linkedin_connected"):
        score += 2

    return round(score, 2)