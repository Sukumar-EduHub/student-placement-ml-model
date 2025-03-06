from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

app = FastAPI()

# Define student input schema
class StudentInput(BaseModel):
    CGPA: float
    Backlogs: int
    Internships: int
    Coding_Skills: int
    Communication_Skills: int
    Projects_Completed: int
    Certifications: int
    Hackathon_Participation: int
    Extracurricular_Activities: int

@app.post("/predict")
def predict(data: StudentInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Ensure column names match training data
    expected_columns = [
        "CGPA", "Backlogs", "Internships", "Coding_Skills", "Communication_Skills",
        "Projects_Completed", "Certifications", "Hackathon_Participation", "Extracurricular_Activities"
    ]
    input_df = input_df.reindex(columns=expected_columns)

    # Predict
    prediction = model.predict(input_df)[0]

    return {"prediction": int(prediction)}

@app.get("/")
def home():
    return {"message": "College Student Placement Prediction API Running"}
