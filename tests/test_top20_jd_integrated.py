from src.utils.data_loader import (
    load_candidates
)

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

from src.jd.jd_parser import (
    parse_job_description
)


with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as f:

    jd_text = f.read()

jd_data = parse_job_description(
    jd_text
)

candidates = load_candidates(
    "data/candidates.jsonl"
)

results = []

for candidate in candidates:

    features = extract_candidate_features(
        candidate
    )

    technical_score = (
        calculate_technical_score(
            features
        )
    )

    signal_score = (
        calculate_signal_score(
            candidate["redrob_signals"]
        )
    )

    experience_score = (
        calculate_experience_score(
            candidate
        )
    )

    ai_score = (
        calculate_ai_relevance_score(
            candidate
        )
    )

    career_credibility = (
        calculate_career_credibility_score(
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

    job_match_score = (
        calculate_job_match_score_v4(
            candidate,
            jd_data
        )
    )

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

    results.append(
        {
            "candidate_id":
                candidate["candidate_id"],

            "title":
                candidate["profile"][
                    "current_title"
                ],

            "final_score":
                round(
                    final_score,
                    2
                ),

            "job_match_score":
                job_match_score,

            "evidence_score":
                evidence_score,

            "production_experience_score":
                production_experience_score
        }
    )

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)

print("\nTOP 20\n")

for result in results[:20]:
    print(result)