import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

# Function to extract text from PDF
def extract_text_from_pdf(file):
    try:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + " "
        return text.strip()
    except Exception as e:
        return ""

# Preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(documents).toarray()
    
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    return cosine_similarities

# Function to generate downloadable report
def generate_download_link(df):
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    b64 = base64.b64encode(output.read()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="resume_ranking.csv">📥 Download Ranking Report</a>'

# Streamlit UI
st.set_page_config(page_title="AI Resume Screening System", layout="wide")
st.title("📝 AI Resume Screening & Candidate Ranking System")
st.write("Upload resumes and compare them against the job description to rank candidates.")

# Job description input
st.subheader("📄 Job Description")
job_description = st.text_area("Enter the job description", height=150)

# File uploader
st.subheader("📂 Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.subheader("📊 Ranking Results")
    
    job_description = preprocess_text(job_description)
    resumes = []
    resume_names = []
    
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        text = preprocess_text(text)
        if text:
            resumes.append(text)
            resume_names.append(file.name)
    
    if resumes:
        scores = rank_resumes(job_description, resumes)
        results = pd.DataFrame({"Resume": resume_names, "Score": scores})
        results = results.sort_values(by="Score", ascending=False)
        
        # Display top-ranked resumes
        st.dataframe(results.style.format({'Score': '{:.4f}'}).highlight_max(axis=0, subset=['Score'], color='lightgreen'))
        
        # Visualization
        st.subheader("📊 Resume Ranking Visualization")
        fig, ax = plt.subplots()
        sns.barplot(x=results["Score"], y=results["Resume"], palette="viridis", ax=ax)
        ax.set_xlabel("Similarity Score")
        ax.set_ylabel("Resume")
        ax.set_title("Resume Ranking Visualization")
        st.pyplot(fig)
        
        # Download Results
        st.markdown(generate_download_link(results), unsafe_allow_html=True)
    else:
        st.warning("No valid text extracted from the resumes. Please check your PDF files.")


#streamlit run "D:\AICTE Internship\Code\app.py"