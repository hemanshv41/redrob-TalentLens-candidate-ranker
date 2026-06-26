def calculate_final_score(
    technical_score,
    signal_score,
    experience_score
):

    return round(
        technical_score * 0.5 +
        signal_score * 0.3 +
        experience_score * 0.2,
        2
    )