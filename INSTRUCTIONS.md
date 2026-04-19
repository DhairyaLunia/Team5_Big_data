# Instructions

## Prerequisites

- Databricks Community Edition account
- Yelp Open Dataset downloaded
- Python 3.10+

## Installation

```bash
pip install gensim nltk vaderSentiment sentence-transformers faiss-cpu langchain openai streamlit scipy
```

## How to Run Each Stage

### 1. Data Processing
- Run `01_data_processing/dhairya_etl.ipynb` in Databricks.
- **Expected Output:** `merged_philly` and `businesses_filtered` temp views.

### 2. Topic Modeling
- Run `02_topic_modeling/lear_lda_topics.ipynb` in Databricks.
- **Expected Output:** `lda_topic_results` table with topic distributions per review.

### 3. Feature Engineering
- Run `03_feature_engineering/saloni_feature_engineering.ipynb` in Databricks.
- **Expected Output:** `business_profiles` and `user_personas` tables.

### 4. Recommender RAG
- Run `04_recommender_rag/quinten_faiss_langchain.ipynb` locally or in Databricks.
- **Expected Output:** FAISS index built from `business_profiles`.

### 5. Interface
- Run `streamlit run 05_interface/app.py` locally.
- **Expected Output:** Streamlit web application running on `localhost`.

## Data Flow
- **Data Processing:** Takes raw Yelp JSON -> Outputs filtered views.
- **Topic Modeling:** Takes filtered reviews -> Outputs review-topic associations.
- **Feature Engineering:** Takes topics, businesses, users -> Outputs business and user profiles.
- **Recommender:** Takes business profiles + user prompt -> Outputs recommendations.
- **Interface:** Takes recommended businesses + RAG response -> Outputs user-facing recommendations.

Note: No large data files are stored in this repository. All data operations utilize Databricks FileStore.
