import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

st.title("CONTENT NEST")
st.subheader("AI-Powered Content Idea Generator for Influencers & Creators")
st.caption("Enter your profession and content requirements to get tailored ideas!")

user_prompt = st.text_input("Enter your prompt:")
category = st.text_input("Enter Category", placeholder= "Eg: Lifestyle")
platform = st.selectbox("Select Platform", ["YouTube", "Instagram", "TikTok", "Blog"])
include_hashtags = st.checkbox("Include Hashtags")
include_engagement_tips = st.checkbox("Include Engagement Tips")

if st.button("Generate Ideas"):
    if user_prompt:
        prompt_text = f"""
        You are a creative content strategist. Based on the inputs below, generate 10 innovative and actionable content ideas. Each idea should include a title, a brief description, and optionally include hashtags and engagement tips if specified. The content ideas should be categorized under {category} and specifically tailored for the {platform}.

        User Prompt: {user_prompt}
        Category: {category}
        Platform: {platform}
        {"Include relevant hashtags for each idea." if include_hashtags else ""}
        {"Include engagement tips for each idea." if include_engagement_tips else ""}
        

        Output Format:

        Title: [Concise and catchy title]
        Description: [Brief explanation of the idea and how it works]
        Hashtags: [If requested]
        Engagement Tip: [If requested]
        
        Generate content that is creative, relevant, and platform-specific (e.g., reels for Instagram, threads for X, shorts for YouTube). Avoid repetition and ensure variety in the ideas.


        """

        response = llm.invoke(prompt_text)

        st.subheader("Generated Content Ideas:")
        st.write(response.content)
    else:
        st.warning("Please enter a prompt.")