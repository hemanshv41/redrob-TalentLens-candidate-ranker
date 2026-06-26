from src.features.candidate_features import (
    extract_candidate_features
)

from src.scoring.technical_scorer import (
    calculate_technical_score
)

from src.scoring.signal_scorer import (
    calculate_signal_score
)

from src.scoring.experience_scorer import (
    calculate_experience_score
)

from src.scoring.ai_relevance_scorer import (
    calculate_ai_relevance_score
)
# from src.scoring.role_affinity_scorer import (
#     calculate_role_affinity_score
# )

from src.scoring.career_affinity_scorer import (
    calculate_career_affinity_score
)

from src.scoring.career_credibility_scorer import (
    calculate_career_credibility_score
)

from src.scoring.production_experience_scorer import (
    calculate_production_experience_score
)

from src.scoring.evidence_scorer import (
    calculate_evidence_score
)

from src.scoring.job_match_scorer_v4 import (
    calculate_job_match_score_v4
)


def rank_candidate(candidate , jd_data=None):

    features = extract_candidate_features(candidate)

    technical_score = calculate_technical_score(
        features
    )

    signal_score = calculate_signal_score(
        candidate["redrob_signals"]
    )

    experience_score = calculate_experience_score(
        candidate
    )

    ai_score = calculate_ai_relevance_score(
        candidate
    )

    career_credibility = (
    calculate_career_credibility_score(
        candidate
    )
)
    
#     role_affinity = (
#     calculate_role_affinity_score(
#         candidate["profile"]["current_title"]
#     )
# )
    career_affinity = (
    calculate_career_affinity_score(
        candidate
    )
)

    production_experience_score = (
    calculate_production_experience_score(
        candidate
    )
)

    evidence_score = (
    calculate_evidence_score(
        candidate
    )
)

#     job_match_score = (
#     calculate_job_match_score_v4(
#         candidate,
#         jd_data
#     )
# )

    job_match_score = 0

    if jd_data is not None:
        job_match_score = (
        calculate_job_match_score_v4(
            candidate,
            jd_data
        )
    )
    # final_score = (
    #     technical_score * 0.20 +
    #     signal_score * 0.20 +
    #     experience_score * 0.15 +
    #     ai_score * 0.45
    # )
#     final_score = (
#     technical_score * 0.15 +
#     signal_score * 0.15 +
#     experience_score * 0.15 +
#     ai_score * 0.35 +
#     role_affinity * 0.20
# )

    # final_score = (
    # technical_score * 0.15
    # + signal_score * 0.15
    # + experience_score * 0.10
    # + ai_score * 0.40
    # + career_affinity * 0.20
    #  )
#     final_score = (
#     technical_score * 0.15
#     + signal_score * 0.15
#     + experience_score * 0.10
#     + ai_score * 0.40
#     + career_credibility * 0.20
# )
#     final_score = (
#     technical_score * 0.15
#     + signal_score * 0.10
#     + experience_score * 0.10
#     + ai_score * 0.25
#     + career_credibility * 0.15
#     + production_experience_score * 0.25
# )

#     final_score = (
#     technical_score * 0.10
#     + signal_score * 0.10
#     + experience_score * 0.05
#     + ai_score * 0.20
#     + career_credibility * 0.15
#     + production_experience_score * 0.25
#     + evidence_score * 0.15
# )

    final_score = (
    technical_score * 0.10
    + signal_score * 0.10
    + experience_score * 0.05
    + ai_score * 0.20
    + career_credibility * 0.15
    + production_experience_score * 0.15
    + evidence_score * 0.10
    + job_match_score * 0.15
)
    # return {
    #     "candidate_id": candidate["candidate_id"],
    #     "title": candidate["profile"]["current_title"],
    #     "technical_score": technical_score,
    #     "signal_score": signal_score,
    #     "experience_score": experience_score,
    #     "ai_score": ai_score,
    #     "final_score": round(final_score, 2)
    # }
#     return {
#     "candidate_id": candidate["candidate_id"],
#     "title": candidate["profile"]["current_title"],
#     "technical_score": technical_score,
#     "signal_score": signal_score,
#     "experience_score": experience_score,
#     "ai_score": ai_score,
#     "role_affinity": role_affinity,
#     "final_score": round(final_score, 2)
# }
    return {
    "candidate_id": candidate["candidate_id"],
    "title": candidate["profile"]["current_title"],
    "technical_score": technical_score,
    "signal_score": signal_score,
    "experience_score": experience_score,
    "ai_score": ai_score,
    "career_credibility": career_credibility,
    "production_experience_score": production_experience_score,
    "evidence_score": evidence_score,
    "job_match_score": job_match_score,
    "final_score": round(final_score, 2)
}





def rank_candidates(candidates , jd_data=None):

    results = []

    for candidate in candidates:

        result = rank_candidate(
            candidate , 
            jd_data
        )

        results.append(
            result
        )

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results