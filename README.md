# PersonaPath

Context-Aware Travel & Dining Recommendation Engine using RAG & Behavioral Personas. Built on Yelp Open Dataset (6.9M reviews).

## Team Members and Roles

| Name | Role |
| :--- | :--- |
| Dhairya Lunia | 01_data_processing |
| Fu Lee (Lear) | 02_topic_modeling |
| Saloni Jain | 03_feature_engineering |
| Hsin Kuei Chang (Quinten) | 04_recommender_rag |
| Esther Baumgartner | 05_interface |

## Pipeline Overview

Data Processing → Topic Modeling → Feature Engineering → Recommender System → Interface

## Dataset

Yelp Open Dataset: [https://www.yelp.com/dataset](https://www.yelp.com/dataset)

## Tech Stack

| Component | Technologies |
| :--- | :--- |
| **Data Processing** | PySpark, Databricks Community Edition, Delta Lake |
| **Topic Modeling** | Gensim LDA, NLTK |
| **Feature Engineering** | VADER Sentiment, Spark MLlib K-Means |
| **Recommender System**| FAISS, LangChain, GPT-4o/Claude API |
| **Interface** | Streamlit |

## How to Run

Please see [INSTRUCTIONS.md](INSTRUCTIONS.md) for detailed step-by-step setup and execution instructions for each stage of the pipeline.

This project repository is created in partial fulfillment of the requirements for the Big Data Analytics course offered by the Master of Science in Business Analytics program at the Carlson School of Management, University of Minnesota.

## Links
- [Yelp Open Dataset](https://www.yelp.com/dataset)
- [Team Flier (Placeholder)](#)
- [Paper References](#)
