# AI_KEYWORDS = {
#     "Machine Learning",
#     "Deep Learning",
#     "NLP",
#     "Computer Vision",
#     "PyTorch",
#     "TensorFlow",
#     "RAG",
#     "Embeddings",
#     "FAISS",
#     "Milvus",
#     "Pinecone",
#     "Sentence Transformers",
#     "LLMs",
#     "LangChain",
#     "Fine-tuning LLMs",
#     "Recommendation Systems",
#     "Information Retrieval",
# }

AI_KEYWORDS = {
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Computer Vision",
    "PyTorch",
    "TensorFlow",

    "LLMs",
    "RAG",
    "Embeddings",
    "Sentence Transformers",
    "FAISS",
    "Milvus",
    "Pinecone",
    "Qdrant",
    "Weaviate",

    "LangChain",
    "Fine-tuning LLMs",
    "LoRA",
    "QLoRA",

    "Recommendation Systems",
    "Information Retrieval",
    "Semantic Search",

    "Vector Search",
    "Vector Databases",

    "Ranking",
    "Hybrid Search",
    "Retrieval",

    "A/B Testing",
    "Evaluation Frameworks"
}


def parse_job_description(text):

    found_skills = []

    lower_text = text.lower()

    for skill in AI_KEYWORDS:

        if skill.lower() in lower_text:
            found_skills.append(skill)

    return {
        "required_skills": found_skills
    }