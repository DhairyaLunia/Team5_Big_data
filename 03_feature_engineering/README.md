# 03 Feature Engineering

This stage aggregates topic vectors per business and user. It also scores reviews using VADER sentiment analysis, assigns the dominant vibe tag, calculates K-Means persona clustering (k=6) to establish user personas, and outputs persona confidence scores and intent combo scores.

It outputs the `business_profiles` and `user_personas` datasets.
