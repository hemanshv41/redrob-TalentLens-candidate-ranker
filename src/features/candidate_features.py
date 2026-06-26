from src.features.skill_taxonomy import (
    AI_SKILLS,
    LLM_SKILLS,
    RETRIEVAL_SKILLS,
    DATA_ENGINEERING_SKILLS,
    CLOUD_SKILLS
)


def extract_candidate_features(candidate):

    skills = candidate.get("skills", [])

    skill_names = {
        skill["name"]
        for skill in skills
    }

    features = {
        "ai_skill_count": len(skill_names & AI_SKILLS),
        "llm_skill_count": len(skill_names & LLM_SKILLS),
        "retrieval_skill_count": len(skill_names & RETRIEVAL_SKILLS),
        "data_skill_count": len(skill_names & DATA_ENGINEERING_SKILLS),
        "cloud_skill_count": len(skill_names & CLOUD_SKILLS),
    }

    return features