from src.features.skill_taxonomy import (
    AI_SKILLS,
    LLM_SKILLS,
    RETRIEVAL_SKILLS,
)

def calculate_ai_relevance_score(candidate):

    skills = candidate.get("skills", [])

    skill_names = {
        skill["name"]
        for skill in skills
    }

    score = 0

    score += len(
        skill_names & AI_SKILLS
    ) * 10

    score += len(
        skill_names & LLM_SKILLS
    ) * 15

    score += len(
        skill_names & RETRIEVAL_SKILLS
    ) * 20

    return min(score, 100)