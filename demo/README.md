# PersonaPath: Quick Engine Demo

This directory provides a quick walkthrough of how the PersonaPath recommendation engine processes data to deliver personalized dining experiences.

## 🏁 Quick Start: The "Concierge" Demo

To see the engine in action right now, the best way is to run our interactive dashboard:

```bash
# From the root directory
streamlit run notebooks/05_streamlit_interface.py
```

## 🧠 How the Engine Works (The 4-Layer Process)

### Step 1: Behavioral Persona Matching
The engine looks at your historical "Taste DNA." If you frequently visit quiet, high-quality coffee shops, your persona vector will align with our **"Solo Focus"** and **"Premium Quality"** topics.
*   **Metric:** Cosine Similarity between User Persona and Business Profile vectors.

### Step 2: Intent Boosting
Are you looking for a **Romantic Date** or a **Family Dinner**? Our intent-based scoring (Layer 2) applies a 0.3 weight boost to businesses that specifically match your current query intent.

### Step 3: Quality Validation (EAS Score)
We don't just recommend what matches—we recommend what's *good*. The **EAS Quality Score** filters for businesses with high sentiment, low topic entropy (consistency), and a healthy volume of reviews.

### Step 4: Natural Language Explanation
Instead of just a list, our **LLM Concierge** generates a reason:
> *"I recommend 'The Daily Grind' because your history shows a preference for quiet workspaces, and this location has a 0.92 intent score for 'Solo Work' with positive sentiment regarding its Wi-Fi and seating."*

---

### 📂 Demo Assets
*   **Presentation Deck:** [Link to PDF/PPT here]
*   **Engine Walkthrough Video:** `PersonaPath_Demo.mp4`
