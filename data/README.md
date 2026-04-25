# Data Schema & Output Tables

The PersonaPath pipeline generates two primary output tables in Delta Lake.

## 1. `business_profiles`
*   **Total Records:** 1,962 restaurants
*   **Total Columns:** 48

| Column Group | Description |
| :--- | :--- |
| **Metadata** | `business_id`, `name`, `address`, `city`, `is_open`, `stars`, `review_count`, plus hours for all 7 days. |
| **Topic Vectors (25 cols)** | Normalized probability scores for each of the 25 behavioral topics (e.g., `topic_01`, `topic_02`...). |
| **Intent Scores (5 cols)** | Proprietary scores for: `romantic`, `solo_work`, `family`, `group`, `hidden_gem`. |
| **Quality Metrics** | `vader_sentiment` (aggregated average) and the final `EAS_score`. |

## 2. `user_personas`
*   **Total Records:** 20,017 users

| Column | Description |
| :--- | :--- |
| **`user_id`** | Unique identifier for the Yelp user. |
| **Topic Vectors (25 cols)** | The user's historical behavioral DNA based on their review history. |
| **`top_3_topics`** | The most dominant behavioral preferences for the user. |
| **`confidence_score`** | Statistical confidence in the persona assignment (based on review count and topic consistency). |

---

### Delta Lake Configuration
*   **Location:** `msbabigdata.default`
*   **Write Mode:** `overwriteSchema=True` (Ensures clean updates even if columns are added or modified during feature engineering).
