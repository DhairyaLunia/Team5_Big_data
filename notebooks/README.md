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

Prerequisites

Python 3.9+
OpenAI API key
Google Places API key

Setup
bashpip install streamlit pandas numpy scikit-learn openai requests plotly pydeck scipy
Open big_data.py and fill in your credentials near the top:
pythonOPENAI_API_KEY    = "sk-..."
GOOGLE_PLACES_KEY = "AIza..."
Also update the two hardcoded data paths in load_data() to point to your local CSV files:
pythonb_path = "/path/to/business_profiles.csv"
u_path = "/path/to/user_personas.csv"
Run
bashstreamlit run big_data.py

Note: The app expects two CSVs — business_profiles.csv and user_personas.csv — with the topic score columns and fields referenced in the code. If you're sharing those datasets publicly, add them to the repo and update the paths to relative ones (e.g. "data/business_profiles.csv"), which will make the setup one step simpler for anyone cloning it.
