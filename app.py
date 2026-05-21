
import streamlit as st
from utils.parser import extract_text
from utils.skills import extract_skills
from utils.career import recommend_career

st.set_page_config(
    page_title="AI Career Screening",
    layout="wide"
)

st.title("🚀 AI Career Screening Platform")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    careers = recommend_career(skills)

    st.subheader("✅ Extracted Skills")
    st.write(skills)

    st.subheader("🎯 Career Recommendations")

    for career in careers:

        st.markdown(f"""
        ### {career['career']}
        Match Score: {career['score']}%

        Salary: {career['salary']}

        Roadmap:
        {career['roadmap']}
        """)
