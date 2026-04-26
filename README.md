# PersonaPath: Personalized Travel & Dining Recommendation Engine
### *Beyond Proximity: A Behavioral-Driven Discovery Engine for the Modern Diner*

[![PersonaPath](https://img.shields.io/badge/PersonaPath-v1.0-blue?style=for-the-badge&logo=openai)](https://github.com/DhairyaLunia/Team5_Big_data)
[![Apache Spark](https://img.shields.io/badge/Distributed_Processing-Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Gensim](https://img.shields.io/badge/Behavioral_Modeling-Gensim_LDA-blue?style=for-the-badge)](https://radimrehurek.com/gensim/)
[![FAISS](https://img.shields.io/badge/Vector_Search-FAISS-0433FF?style=for-the-badge&logo=facebook&logoColor=white)](https://github.com/facebookresearch/faiss)

---

## 🌟 Executive Summary
Traditional recommendation platforms (like Yelp or Google Maps) answer the question: *"What is nearby?"* **PersonaPath** answers the question: *"Who am I, and where should I go?"*

Built by **Team 5 at the Carlson School of Management (MSBA)**, PersonaPath is a sophisticated recommendation engine that leverages 6.9 million Yelp reviews to build deep behavioral profiles. By combining **LDA Topic Modeling**, **VADER Sentiment Analysis**, and **FAISS-powered Vector Search**, we deliver personalized dining matches with natural language justifications.

---

## 🏗️ The PersonaPath Engine: 4-Layer Architecture
Our recommendation logic is built on a proprietary four-layer weighted scoring system that balances historical behavior, current intent, and absolute quality.

| Layer | Component | Weight | Logic |
| :--- | :--- | :--- | :--- |
| **Layer 1** | **Behavioral DNA** | **0.50** | 25-dimensional topic vectors calculated per business and user using LDA. Matches users with the "vibe" of a restaurant. |
| **Layer 2** | **Query Intent Boost** | **0.30** | Dynamic intent scoring for 5 personas: *Romantic, Solo Work, Family, Group, Hidden Gem*. |
| **Layer 3** | **EAS Quality Score** | **0.20** | `Sentiment × (1 - Topic Entropy) × Log(Review Count)`. Penalizes inconsistency and rewards established excellence. |
| **Layer 4** | **LLM Concierge** | **N/A** | RAG pipeline using FAISS retrieval and GPT-4o to generate natural language explanations for every recommendation. |

---

## 🔬 Key Technical Innovations
### 1. Behavioral Isolation (The "Cuisine-Blind" LDA)
To prevent the engine from simply matching cuisine types (which is already handled by categorical filters), we surgically removed **99 cuisine-specific words** (e.g., *sushi, taco, pizza*) from the LDA corpus. This forced the model to learn **behaviors** (e.g., *attentive service, quiet atmosphere, efficient takeout*) rather than just food categories.

### 2. The EAS Quality Metric
We developed the **Entropy-Adjusted Sentiment (EAS)** score to solve the "generic rating" problem. By multiplying sentiment with the inverse of topic entropy, we identify businesses that are not just highly rated, but **consistently great at their core persona**.

### 3. Distributed Scale
Processing 6.9 million reviews across thousands of users required a distributed approach. Using **Apache Spark on Databricks**, we implemented a high-performance pipeline that persists data in **Delta Lake** for schema reliability and rapid retrieval.

---

## 👥 The Team
*   **Saloni Jain:** Lead for LDA Behavioral Modeling and Feature Engineering.
*   **Quinten:** Architect of the RAG Pipeline and FAISS Vector Similarity search.
*   **Dhairya:** Model Optimization and technical support.
*   **Esther:** Designer of the Streamlit Interface and the PersonaPath Flier.
*   **Lear:** Presentation Strategy and LDA Data Pipeline orchestration.

---

## 📊 Project Impact (Philadelphia Subset)
*   **1,962** Restaurants profiled across 48 behavioral and intent features.
*   **20,017** Unique User Personas built from historical dining patterns.
*   **261,000** High-quality reviews analyzed for sentiment and topic distribution.

---

## 🔗 Resources & Navigation
*   🚀 **[Quick Start Guide](INSTRUCTIONS.md)** - How to run the pipeline.
*   📓 **[Notebooks Directory](./notebooks/)** - All 5 core scripts (Data Processing to Interface).
*   📁 **[Demo Walkthrough](./demo/)** - See the engine and walkthrough video in action.
*   📄 **[Project Flyer](./flier/Team5_PersonaPath_Flier.pdf)** - Executive summary PDF.
*   📚 **[Bibliography](./BIBLIOGRAPHY.md)** - Data and library credits.

---

> This project repository is created in partial fulfillment of the requirements for the Big Data Analytics course offered by the Master of Science in Business Analytics program at the Carlson School of Management, University of Minnesota.
