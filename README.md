# PersonaPath: Personalized Travel & Dining Recommendation Engine

![PersonaPath Logo](https://img.shields.io/badge/PersonaPath-Project-blue?style=for-the-badge&logo=openai)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

PersonaPath is a state-of-the-art personalized restaurant recommendation system for Philadelphia that leverages **Retrieval Augmented Generation (RAG)** and **behavioral profiling** on 6.9 million Yelp reviews.

## 🚀 Overview

Traditional recommendation platforms tell you **WHAT** is nearby (distance, rating, price). PersonaPath tells you **WHO** you are and matches you with dining experiences that fit your specific persona—delivering recommendations with natural language explanations.

## 🏗️ System Architecture (4-Layer Engine)

Our recommendation engine operates across four sophisticated layers:

1.  **Layer 1 — Behavioral Persona (0.5 weight):** 25-dimensional topic vectors calculated using LDA for every business and user.
2.  **Layer 2 — Query Intent Boost (0.3 weight):** Real-time intent scoring across 5 categories (*romantic, solo work, family, group, hidden gem*) plus hard filters for cuisine.
3.  **Layer 3 — EAS Quality Score (0.2 weight):** A custom quality metric: `Sentiment × (1 - Topic Entropy) × Log(Review Count)`.
4.  **Layer 4 — LLM Concierge:** Generates natural language justifications for each recommendation based on the user's specific "Taste DNA."

## 🛠️ Tech Stack

*   **Distributed Processing:** Apache Spark on Databricks
*   **Behavioral Modeling:** Gensim LDA (25-topic model)
*   **Sentiment Analysis:** VADER Sentiment Analysis
*   **Vector Search:** FAISS (Facebook AI Similarity Search)
*   **Data Lake:** Delta Lake (with schema evolution)
*   **Languages/Tools:** Python, PySpark, Streamlit, NLTK
*   **Dataset:** Yelp Open Dataset (Philadelphia Subset: 1,962 restaurants, 20,017 users, 261K reviews)

## 👥 Team 5 Members & Roles

| Name | Role |
| :--- | :--- |
| **Saloni Jain** | LDA Topic Modeling + Feature Engineering |
| **Quinten** | RAG Pipeline + FAISS Vector Search |
| **Dhairya** | Model Support |
| **Esther** | Streamlit UI + Project Flyer |
| **Lear** | Deck + LDA Data Pipeline |

## 📊 Results Summary

*   **1,962** Businesses profiled with rich metadata and intent scores.
*   **20,017** Unique user personas built from historical behavioral data.
*   **25** Distinct behavioral topics discovered (e.g., "Fine Dining Excellence," "Casual Brunch Vibes").

## 🔗 Project Links

*   **Dataset:** [Yelp Open Dataset](https://www.yelp.com/dataset)
*   **Demo:** [PersonaPath Streamlit App](https://github.com/DhairyaLunia/Team5_Big_data.git)
*   **Documentation:** [Project Flyer & Deck](./flier/)

---

## ⚡ Quick Start

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/DhairyaLunia/Team5_Big_data.git
    ```
2.  **Review Instructions:** See [INSTRUCTIONS.md](INSTRUCTIONS.md) for environment setup and notebook execution order.

---

> This project repository is created in partial fulfillment of the requirements for the Big Data Analytics course offered by the Master of Science in Business Analytics program at the Carlson School of Management, University of Minnesota.
