def calculate_technical_score(features):

    score = 0

    score += features["ai_skill_count"] * 10

    score += features["llm_skill_count"] * 15

    score += features["retrieval_skill_count"] * 20

    score += features["data_skill_count"] * 5

    score += features["cloud_skill_count"] * 5

    return min(score, 100)