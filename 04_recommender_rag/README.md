# 04 Recommender RAG

This stage builds a FAISS index on business embeddings. It sets up a LangChain agent using a system prompt that handles requests from both existing and new users. This includes a 3-layer hallucination prevention system and cold start onboarding flow.
