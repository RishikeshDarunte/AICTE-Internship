# AI Resume Screening & Candidate Ranking System

![AI Resume Screening](https://img.shields.io/badge/AI%20Resume%20Screening-Python%20%7C%20Flask%20%7C%20Scikit--learn%20%7C%20NLP-blue)


## 📌 Project Overview
This project was developed as part of the **AICTE Internship on AI: Transformative Learning with TechSaksham**. It is an **AI-powered Resume Screening System** that ranks candidates based on job descriptions using **TF-IDF vectorization** and **cosine similarity**. The system extracts text from **PDF resumes**, preprocesses the content, and compares it against the job description to generate similarity scores.

![Resume Screening System](https://github.com/RishikeshDarunte/AICTE-Internship/blob/main/Img/Dashboard.png)
---

## 🎯 Key Features
- ✅ **Automated Resume Ranking** based on job relevance  
- ✅ **TF-IDF & Cosine Similarity** for text matching  
- ✅ **Interactive UI** built with **Streamlit**  
- ✅ **Data Visualization** using **Seaborn** & **Matplotlib**  
- ✅ **Downloadable Ranking Report** in CSV format  
- ✅ **Error Handling & Preprocessing** for improved accuracy  
---

## 🛠️ Technologies Used
- **Python**
- **Streamlit** (for UI)
- **PyPDF2** (for extracting text from PDFs)
- **Scikit-learn** (for TF-IDF and cosine similarity)
- **Matplotlib & Seaborn** (for data visualization)
- **Pandas & NumPy** (for data processing)
---

## 🚀 How It Works
1. **Upload resumes** (PDF format).
2. **Enter Job Description** in the provided text box.
3. The system **ranks resumes** based on similarity scores.
4. **View results** with a bar chart and data table.
5. **Download the ranking report** as a CSV file.   
---

## 📥 Installation & Setup

### Prerequisites

- Ensure you have Python 3.x installed.
---

## Install Dependencies

-To install the required Python packages, run the following command:

    
    pip install streamlit PyPDF2 pandas numpy scikit-learn matplotlib seaborn
    
---

## 🚀 Running the Application

-To start the application, navigate to the project directory and run:
  
    
    streamlit run app.py
    

