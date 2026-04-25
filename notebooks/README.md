# Project Scripts & Notebooks

This directory contains the complete PersonaPath analytics pipeline, including data processing, modeling, and the user interface.

| File | Purpose (Plain English) |
| :--- | :--- |
| **`01_data_processing.ipynb`** | **The Filter:** Cleans the raw Yelp data to extract the Philadelphia subset. |
| **`02_lda_topic_modeling.ipynb`** | **The Brain:** Trains the 25-topic behavioral model (removes 99 cuisine words). |
| **`03_feature_engineering.ipynb`** | **The Profiler:** Creates "Taste DNA" profiles for restaurants and users. |
| **`04_recommender_rag.ipynb`** | **The Oracle:** Handles vector search and natural language explanations. |
| **`05_streamlit_interface.py`** | **The Window:** The interactive Streamlit dashboard for the end-user. |

---

### Key Technical Decisions
*   **Centralized Scripts:** All core logic is centralized here for easy version control and execution.
*   **Cuisine Word Removal:** 99 cuisine words removed from LDA to prevent signal duplication.
*   **Delta Lake Compatibility:** Cleaned column names for Delta table integration.
