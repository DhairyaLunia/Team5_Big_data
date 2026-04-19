import streamlit as st

def main():
    st.set_page_config(page_title=\"SentimenTrip\", page_icon=\"✈️\", layout=\"wide\")
    
    st.title(\"SentimenTrip\")
    st.subheader(\"Context-Aware Travel & Dining Recommendation Engine\")
    
    st.sidebar.header(\"User Flow Profile\")
    user_type = st.sidebar.radio(\"User Type\", [\"Existing User\", \"New User (Cold Start)\"])
    
    if user_type == \"Existing User\":
        st.sidebar.markdown(\"### Persona Card\")
        st.sidebar.success(\"**Persona:** The Comfort Seeker\\n\\n**Vibe Preference:** Cozy, Family-Friendly\")
    else:
        st.sidebar.markdown(\"### Onboarding\")
        st.sidebar.info(\"Please select your current vibe/intent to generate temporary persona.\")
    
    st.markdown(\"### How can I help you today?\")
    
    # 5 Demo queries placeholder
    st.markdown(\"**Demo Queries:**\")
    demo_queries = [
        \"I want a romantic Italian restaurant for a date night.\",
        \"Where can I get the best spicy food with fast service?\",
        \"Looking for a quiet coffee shop with vegan options to study.\",
        \"Need a family-friendly place with large portions.\",
        \"What is the highest-rated authentic Latin food around here?\"
    ]
    for q in demo_queries:
        if st.button(q):
            st.session_state.query = q
            
    query = st.chat_input(\"Type your request here...\")
    
    if query or st.session_state.get('query'):
        st.write(f\"**Searching for:** {query or st.session_state.get('query')}\")
        st.markdown(\"---\")
        
        # Results cards placeholder
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(\"#### Result 1: The Fancy Fork\")
            st.caption(\"Vibe Tags: [Romantic] [Italian] [Date Night]\")
            st.write(\"**Agent Citation:** Based on 15 reviews mentioning 'great ambiance for dates', I recommend The Fancy Fork.\")
        with col2:
            st.markdown(\"#### Result 2: Pasta Express\")
            st.caption(\"Vibe Tags: [Fast] [Italian] [Value]\")
            st.write(\"**Agent Citation:** If you prioritize speed, Pasta Express is frequently cited for 'quick service and good value'.\")

if __name__ == \"__main__\":
    main()
