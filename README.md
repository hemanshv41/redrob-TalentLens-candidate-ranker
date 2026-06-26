# 🤖 TalentLens AI Candidate Ranker

TalentLens AI is an advanced, multi-factor candidate ranking system designed to automatically score, rank, and evaluate candidate profiles for technical roles, with a focus on Search, Retrieval, Recommendation, and Machine Learning/AI engineering positions.

The application features a sleek, interactive Streamlit web interface with a modern glassmorphism design, allowing recruiters to paste a job description and instantaneously identify the best-matching talent.

---

## 🚀 Key Features

* **Multi-Factor Scoring Engine:** Ranks candidates based on 8 distinct technical and career dimensions.
* **Semantic Job Description Matching:** Automatically parses JD requirements to match candidate skills, history, and job titles.
* **AI-Generated Explanations:** Explains the ranking logic for the top match to provide clear reasoning.
* **Premium User Interface:** A fully responsive Streamlit dashboard featuring glassmorphism design, smooth animated backgrounds, and dynamic metrics.
* **Exportable Reports:** Download the top 100 candidate ranking results as a formatted CSV file.

---

## 📊 Scoring Signals Breakdown

The system computes a `final_score` (rounded to 2 decimal places) using a weighted combination of 8 signals:

| Scoring Signal | Weight | Focus Area |
| :--- | :--- | :--- |
| **AI Relevance Score** | `20%` | General alignment with AI, ML, and Deep Learning paradigms. |
| **Career Credibility** | `15%` | Career longevity, lack of gaps, and candidate stability. |
| **Production Experience** | `15%` | Practical MLOps and production pipelines (e.g., PySpark, streaming, real-time, APIs). |
| **Job Match Score** | `15%` | Specific overlap with the entered Job Description (skills, history, titles). |
| **Technical Score** | `10%` | Core technical skills profile and tool stack. |
| **Signal Score** | `10%` | Recruiter engagement signals (`redrob_signals`). |
| **Evidence Score** | `10%` | Evidence of accomplishments, repositories, and concrete achievements. |
| **Experience Score** | `5%` | Overall professional experience duration. |

---

## 🛠️ Project Structure

```text
├── data/                       # Candidate datasets (demo & full datasets)
├── docs/                       # Project schemas, specifications, and guidance
├── notebooks/                  # Jupyter notebooks for data exploration and scoring development
├── src/                        # Core codebase
│   ├── features/               # Candidate feature extractors
│   ├── jd/                     # Job description parsers
│   ├── ranking/                # Core candidate ranking engine
│   ├── reasoning/              # Explanation & reasoning generator
│   ├── scoring/                # Scoring algorithms for each of the 8 signals
│   ├── semantic/               # Semantic similarity helpers
│   └── utils/                  # Data loaders and general utilities
├── app.py                      # Main Streamlit web application
├── main.py                     # Entry point CLI
├── submission_metadata.yaml    # Submission registry details
└── requirements.txt            # Python dependencies
```

---

## 💻 Installation & Setup

### Prerequisites
* Python 3.10+
* Git

### 1. Clone & Navigate to Repository
```bash
git clone https://github.com/hemanshv41/redrob-TalentLens-candidate-ranker.git
cd redrob-TalentLens-candidate-ranker
```

### 2. Install Dependencies
Install all the required Python packages:
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application

To launch the interactive dashboard, run:
```bash
streamlit run app.py
```

Once running, the application will open automatically in your browser (typically at `http://localhost:8501`).

### How to Use:
1. **View Dataset Context:** The dashboard automatically detects whether you are running on the demo or full dataset and displays metrics of loaded candidates.
2. **Input Job Description:** Paste the target Job Description in the text area (a default AI Engineer JD is pre-filled).
3. **Rank Candidates:** Click on **🚀 Rank Candidates**. The engine parses, matches, scores, and sorts all candidates.
4. **Inspect Results:**
   * Review detected JD skills.
   * View the **Best Match** candidate alongside their match metric, score, and generated reasoning explanation.
   * Browse a summary table of the **Top 20 Ranked Candidates**.
5. **Download Report:** Click **Download Top 100 CSV** to export the ranked list of the best 100 candidates.
