# Setup & Execution Instructions

Follow these steps to set up the PersonaPath pipeline and run the recommendation engine. All scripts and notebooks are located in the `notebooks/` directory.

## 📋 Prerequisites

*   **Databricks Account:** Community Edition or Professional.
*   **Python:** 3.9+
*   **Databricks Catalog:** All tables are stored in `msbabigdata.default`.
*   **Required Python Packages:**
    ```bash
    pip install gensim nltk vaderSentiment pyspark faiss-cpu streamlit
    ```

## 🚀 Step-by-Step Setup (All in `notebooks/`)

### 1. Data Ingestion
Begin by running the ETL process to filter the Philadelphia subset from the Yelp Open Dataset.
*   **Script:** `notebooks/01_data_processing.ipynb`

### 2. Behavioral Modeling (LDA Pipeline)
**[IMPORTANT]** Run this notebook first to generate the 25 topic vectors.
*   **Script:** `notebooks/02_lda_topic_modeling.ipynb`
*   **Tasks:** Data loading, preprocessing (cuisine word removal), LDA training, and topic labeling.

### 3. Feature Engineering
**[IMPORTANT]** Run this notebook second to build the final profiles.
*   **Script:** `notebooks/03_feature_engineering.ipynb`
*   **Tasks:** Generates business profiles (intent scores, sentiment, EAS) and user personas.

### 4. Vector Similarity & RAG
Build the FAISS index and set up the retrieval pipeline.
*   **Script:** `notebooks/04_recommender_rag.ipynb`

### 5. Streamlit UI
To launch the interactive demo:
```bash
streamlit run notebooks/05_streamlit_interface.py
```

## 🛠️ Important Notes
*   **Catalog Paths:** Ensure your Databricks environment points to `msbabigdata.default`.
*   **Clean Saves:** All Delta tables use `overwriteSchema=True`.
*   **Cuisine Filtering:** Cuisine words are removed during LDA training to prevent signal duplication.
