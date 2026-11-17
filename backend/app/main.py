
from fastapi import FastAPI

app = FastAPI(
    title="Freelancer Invoice & Payment Tracker",
    description="API for managing freelance clients, invoices and payments.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Freelancer Invoice & Payment Tracker API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
