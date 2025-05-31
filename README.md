# 🪺 Content Nest – An AI Content Idea Generator

**Content Nest** is an AI-powered application that generates personalized, innovative, and actionable content ideas for influencers, marketers, and content creators based on their profession, platform, and category of interest. Built using **Streamlit** and powered by **Google's Gemini LLM** via **Langchain**, this tool simplifies content planning with just a few user inputs.

---

## 📌 Project Overview

The aim of **Content Nest** is to help digital creators overcome creative blocks by instantly generating 10 tailored content ideas that suit their niche and preferred social platform. The app allows users to:

- Input their profession and content needs.
- Choose a category and target platform (YouTube, Instagram, TikTok, or Blog).
- Optionally request hashtags and engagement tips.
- Receive unique content ideas optimized for their selected platform.

---

## 🧰 Technical Specifications

### 🛠️ Tools & Frameworks

- **Streamlit**: Web app framework for interactive UI.
- **Langchain**: Framework for LLM-based applications.
- **Google Generative AI (Gemini)**: LLM backend used to generate content.
- **Python-dotenv**: Manages environment variables for API keys.

### 💻 Languages & Technologies

- **Python 3**
- **LLM APIs (Gemini via Langchain)**
- **Environment Variables (.env)**

---

## 🔄 System Workflow

1. **User Interface (Streamlit)**  
   - User inputs a content prompt, selects category and platform.  
   - Optionally checks boxes to include hashtags and engagement tips.

2. **Prompt Creation**  
   - Inputs are formatted into a structured prompt designed to elicit detailed responses from the Gemini model.

3. **LLM Invocation**  
   - The prompt is sent to the Gemini model via `langchain_google_genai.ChatGoogleGenerativeAI`.

4. **Response Display**  
   - The returned ideas are parsed and displayed as a list on the Streamlit app interface.
