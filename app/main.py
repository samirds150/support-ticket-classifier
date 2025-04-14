import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Get the absolute path to the model directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "ticket_model.joblib")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.joblib")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

app = FastAPI()

class TicketRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Support Ticket Classifier is running!"}

@app.post("/predict")
def predict_ticket(ticket: TicketRequest):
    cleaned = ticket.text.lower()
    transformed = vectorizer.transform([cleaned])
    prediction = model.predict(transformed)
    return {"category": prediction[0]}
