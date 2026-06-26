from src.utils.data_loader import load_candidates

from src.jd.jd_parser import (
    parse_job_description
)

from src.scoring.job_match_scorer_v3 import (
    SKILL_ALIASES
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

candidate = next(
    c for c in candidates
    if c["candidate_id"] == "CAND_0003324"
)

skills_text = " ".join(
    skill["name"].lower()
    for skill in candidate["skills"]
)

description_text = " ".join(
    role["description"].lower()
    for role in candidate["career_history"]
)

print(
    "TITLE:",
    candidate["profile"]["current_title"]
)

for jd_skill in jd_data[
    "required_skills"
]:

    aliases = SKILL_ALIASES.get(
        jd_skill.lower(),
        [jd_skill.lower()]
    )

    print("\n" + "=" * 50)
    print("JD SKILL:", jd_skill)

    for alias in aliases:

        if alias in skills_text:

            print(
                "SKILL MATCH:",
                alias
            )

        if alias in description_text:

            print(
                "DESCRIPTION MATCH:",
                alias
            )