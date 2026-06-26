import os
import streamlit as st
import pandas as pd

from src.utils.data_loader import (
    load_candidates
)

from src.jd.jd_parser import (
    parse_job_description
)

from src.ranking.candidate_ranker import (
    rank_candidates
)

from src.reasoning.explanation_generator import (
    generate_explanation
)


st.set_page_config(
    page_title="TalentLens AI",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for gradient and glass-morphism effects
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    [data-testid="stMainBlockContainer"] {
        backdrop-filter: blur(10px);
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        border-radius: 10px !important;
        backdrop-filter: blur(10px);
    }
    
    .stTextArea textarea::placeholder {
        color: rgba(255, 255, 255, 0.7) !important;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        border-radius: 10px !important;
        color: white !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    [data-testid="stMetricDelta"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 15px;
    }
    
    .stDataFrame {
        background: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    
    [data-testid="stDataFrameResizable"] {
        background: rgba(255, 255, 255, 0.05) !important;
    }
    
    .stSuccess, .stError, .stWarning, .stInfo {
        background: rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    
    h1, h2, h3 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    p, span, label {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    .stMarkdown {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    .stDivider {
        border-color: rgba(255, 255, 255, 0.3) !important;
    }
    
    .stSubheader {
        color: white !important;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    }
    
    [data-testid="stDownloadButton"] button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)


def get_dataset_path():

    if os.path.exists(
        "data/candidates.jsonl"
    ):
        return (
            "data/candidates.jsonl"
        )

    return (
        "data/demo_candidates.jsonl"
    )


@st.cache_data
def load_dataset(
    dataset_path
):
    return load_candidates(
        dataset_path
    )


dataset_path = (
    get_dataset_path()
)


st.title(
    "🤖 RankForge AI Candidate Ranker"
)

st.markdown(
    """
    AI-powered candidate ranking system for
    Search, Retrieval, Recommendation and
    Machine Learning roles.
    """
)

if (
    "demo_candidates.jsonl"
    in dataset_path
):
    st.warning(
        "Running on demo dataset for cloud deployment."
    )

else:
    st.success(
        "Running on full dataset."
    )


col1, col2, col3 = st.columns(3)

with col1:

    if (
        "demo_candidates.jsonl"
        in dataset_path
    ):
        candidate_display = (
            "Demo Dataset"
        )

    else:
        candidate_display = (
            "100,000"
        )

    st.metric(
        "Candidates",
        candidate_display
    )

with col2:

    st.metric(
        "Scoring Signals",
        "8"
    )

with col3:

    st.metric(
        "Output",
        "Top 100"
    )


st.divider()


default_jd = """
We are hiring an AI Engineer with experience in:

- Retrieval
- Ranking
- RAG
- LangChain
- Embeddings
- LLMs
- Recommendation Systems
- A/B Testing
"""


jd_text = st.text_area(
    "Paste Job Description",
    value=default_jd,
    height=250
)


if st.button(
    "🚀 Rank Candidates",
    use_container_width=True
):

    if not jd_text.strip():

        st.error(
            "Please enter a job description."
        )

    else:

        with st.spinner(
            "Loading candidates and ranking..."
        ):

            candidates = load_dataset(
                dataset_path
            )

            jd_data = parse_job_description(
                jd_text
            )

            ranked = rank_candidates(
                candidates,
                jd_data
            )

        st.success(
            f"Successfully ranked {len(ranked)} candidates."
        )

        st.divider()

        st.subheader(
            "📌 Detected JD Skills"
        )

        st.write(
            jd_data[
                "required_skills"
            ]
        )

        st.divider()

        best_candidate = ranked[0]

        st.subheader(
            "🏆 Best Match"
        )

        col1, col2 = st.columns(
            [2, 1]
        )

        with col1:

            st.success(
                f"""
Candidate ID: {best_candidate['candidate_id']}

Role: {best_candidate['title']}

Final Score: {best_candidate['final_score']}
"""
            )

        with col2:

            st.metric(
                "JD Match",
                best_candidate[
                    "job_match_score"
                ]
            )

        st.subheader(
            "🧠 Ranking Reasoning"
        )

        st.info(
            generate_explanation(
                best_candidate
            )
        )

        st.divider()

        st.subheader(
            "📊 Top 20 Ranked Candidates"
        )

        top20_df = pd.DataFrame(
            ranked[:20]
        )

        st.dataframe(
            top20_df[
                [
                    "candidate_id",
                    "title",
                    "final_score",
                    "job_match_score",
                    "production_experience_score",
                    "evidence_score"
                ]
            ],
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "⬇ Download Results"
        )

        top100_df = pd.DataFrame(
            ranked[:100]
        )

        csv_data = top100_df.to_csv(
            index=False
        )

        st.download_button(
            label="Download Top 100 CSV",
            data=csv_data,
            file_name="top100_candidates.csv",
            mime="text/csv"
        )


st.divider()

st.markdown(
    "<p style='text-align: center; font-size: 11px; color: gray;'> made by hemansh </p>",
    unsafe_allow_html=True
)









# # import streamlit as st
# # import pandas as pd

# # from src.utils.data_loader import (
# #     load_candidates
# # )

# # from src.jd.jd_parser import (
# #     parse_job_description
# # )

# # from src.ranking.candidate_ranker import (
# #     rank_candidates
# # )


# # st.set_page_config(
# #     page_title="RankForge AI",
# #     layout="wide"
# # )

# # st.title(
# #     "RankForge AI Candidate Ranker"
# # )

# # col1, col2, col3 = st.columns(3)

# # with col1:
# #     st.metric(
# #         "Candidates",
# #         "100,000"
# #     )

# # with col2:
# #     st.metric(
# #         "Scoring Signals",
# #         "8"
# #     )

# # with col3:
# #     st.metric(
# #         "Output",
# #         "Top 100"
# #     )


# # st.write(
# #     """
# #     AI-powered candidate ranking system for
# #     Search, Retrieval, Recommendation and
# #     Machine Learning roles.
# #     """
# # )




# # jd_text = st.text_area(
# #     "Paste Job Description",
# #     height=250
# # )




# # if st.button(
# #     "Rank Candidates"
# # ):

# #     if not jd_text.strip():

# #         st.error(
# #             "Please enter a job description."
# #         )

# #     else:

# #         with st.spinner(
# #             "Loading candidates and ranking..."
# #         ):

# #             candidates = load_candidates(
# #                 "data/candidates.jsonl"
# #             )

# #             jd_data = parse_job_description(
# #                 jd_text
# #             )

# #             ranked = rank_candidates(
# #                 candidates,
# #                 jd_data
# #             )

# #         st.success(
# #             f"Successfully ranked {len(ranked)} candidates."
# #         )

# #         top20 = pd.DataFrame(
# #             ranked[:20]
# #         )

# #         st.subheader(
# #             "Top 20 Candidates"
# #         )

# #         st.dataframe(
# #             top20[
# #                 [
# #                     "candidate_id",
# #                     "title",
# #                     "final_score",
# #                     "job_match_score",
# #                     "production_experience_score",
# #                     "evidence_score"
# #                 ]
# #             ],
# #             use_container_width=True
# #         )

# #         csv_data = (
# #             pd.DataFrame(
# #                 ranked[:100]
# #             )
# #             .to_csv(
# #                 index=False
# #             )
# #         )

# #         st.download_button(
# #             label="Download Top 100 CSV",
# #             data=csv_data,
# #             file_name="top100_candidates.csv",
# #             mime="text/csv"
# #         )



# import streamlit as st
# import pandas as pd

# from src.utils.data_loader import (
#     load_candidates
# )

# from src.jd.jd_parser import (
#     parse_job_description
# )

# from src.ranking.candidate_ranker import (
#     rank_candidates
# )

# from src.reasoning.explanation_generator import (
#     generate_explanation
# )


# st.set_page_config(
#     page_title="RankForge AI",
#     page_icon="🤖",
#     layout="wide"
# )


# st.title(
#     "🤖 RankForge AI Candidate Ranker"
# )

# st.markdown(
#     """
#     AI-powered candidate ranking system for
#     Search, Retrieval, Recommendation and
#     Machine Learning roles.
#     """
# )


# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric(
#         "Candidates",
#         "100,000"
#     )

# with col2:
#     st.metric(
#         "Scoring Signals",
#         "8"
#     )

# with col3:
#     st.metric(
#         "Output",
#         "Top 100"
#     )


# st.divider()


# default_jd = """
# We are hiring an AI Engineer with experience in:

# - Retrieval
# - Ranking
# - RAG
# - LangChain
# - Embeddings
# - LLMs
# - Recommendation Systems
# - A/B Testing
# """


# jd_text = st.text_area(
#     "Paste Job Description",
#     value=default_jd,
#     height=250
# )


# if st.button(
#     "🚀 Rank Candidates",
#     use_container_width=True
# ):

#     if not jd_text.strip():

#         st.error(
#             "Please enter a job description."
#         )

#     else:

#         with st.spinner(
#             "Loading candidates and ranking..."
#         ):

#             candidates = load_candidates(
#                 "data/candidates.jsonl"
#             )

#             jd_data = parse_job_description(
#                 jd_text
#             )

#             ranked = rank_candidates(
#                 candidates,
#                 jd_data
#             )

#         st.success(
#             f"Successfully ranked {len(ranked)} candidates."
#         )

#         st.divider()

#         st.subheader(
#             "📌 Detected JD Skills"
#         )

#         st.write(
#             jd_data["required_skills"]
#         )

#         st.divider()

#         best_candidate = ranked[0]

#         st.subheader(
#             "🏆 Best Match"
#         )

#         col1, col2 = st.columns(
#             [2, 1]
#         )

#         with col1:

#             st.success(
#                 f"""
#                 Candidate ID: {best_candidate['candidate_id']}

#                 Role: {best_candidate['title']}

#                 Final Score: {best_candidate['final_score']}
#                 """
#             )

#         with col2:

#             st.metric(
#                 "JD Match",
#                 best_candidate[
#                     "job_match_score"
#                 ]
#             )

#         st.subheader(
#             "🧠 Ranking Reasoning"
#         )

#         st.info(
#             generate_explanation(
#                 best_candidate
#             )
#         )

#         st.divider()

#         st.subheader(
#             "📊 Top 20 Ranked Candidates"
#         )

#         top20_df = pd.DataFrame(
#             ranked[:20]
#         )

#         st.dataframe(
#             top20_df[
#                 [
#                     "candidate_id",
#                     "title",
#                     "final_score",
#                     "job_match_score",
#                     "production_experience_score",
#                     "evidence_score"
#                 ]
#             ],
#             use_container_width=True
#         )

#         st.divider()

#         st.subheader(
#             "⬇ Download Results"
#         )

#         top100_df = pd.DataFrame(
#             ranked[:100]
#         )

#         csv_data = top100_df.to_csv(
#             index=False
#         )

#         st.download_button(
#             label="Download Top 100 CSV",
#             data=csv_data,
#             file_name="top100_candidates.csv",
#             mime="text/csv"
#         )