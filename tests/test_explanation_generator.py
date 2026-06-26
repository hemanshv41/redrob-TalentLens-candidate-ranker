from src.reasoning.explanation_generator import (
    generate_explanation
)

sample = {
    "ai_score": 90,
    "career_credibility": 75,
    "production_experience_score": 100,
    "signal_score": 70
}

print(
    generate_explanation(sample)
)