import streamlit as st
import requests

API_URL = "https://student-placement-ml-model-3.onrender.com"

st.title("🎓 Student Placement Prediction")

st.header("Enter Student Details")

# User input fields
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
backlogs = st.number_input("Backlogs", min_value=0, max_value=10, step=1)
internships = st.number_input("Internships", min_value=0, max_value=5, step=1)
coding_skills = st.slider("Coding Skills (1-10)", 1, 10, 5)
communication_skills = st.slider("Communication Skills (1-10)", 1, 10, 5)
projects_completed = st.number_input("Projects Completed", min_value=0, max_value=10, step=1)
certifications = st.number_input("Certifications", min_value=0, max_value=10, step=1)
hackathon_participation = st.number_input("Hackathons Participated", min_value=0, max_value=5, step=1)
extracurricular_activities = st.slider("Extracurricular Activities (1-10)", 1, 10, 5)

# Prepare input data
input_data = {
    "CGPA": cgpa,
    "Backlogs": backlogs,
    "Internships": internships,
    "Coding_Skills": coding_skills,
    "Communication_Skills": communication_skills,
    "Projects_Completed": projects_completed,
    "Certifications": certifications,
    "Hackathon_Participation": hackathon_participation,
    "Extracurricular_Activities": extracurricular_activities
}

if st.button("Predict Placement"):
    response = requests.post(f"{API_URL}/predict", json=input_data)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        result = "Placed" if prediction == 1 else "Not Placed"
        st.success(f"Prediction: {result}")
    else:
        st.error("Error: Could not get a response from the API.")
