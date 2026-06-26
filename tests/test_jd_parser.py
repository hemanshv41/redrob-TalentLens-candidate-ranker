from src.jd.jd_parser import (
    parse_job_description
)

# jd = """
# We are looking for an AI Engineer with
# experience in NLP, RAG, LLMs,
# Sentence Transformers and FAISS.
# """
with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as f:

    jd = f.read()
# result = parse_job_description(jd)
result = parse_job_description(jd)

print(result)
