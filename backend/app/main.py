from fastapi import FastAPI

app = FastAPI(
    title="Customer Success TTV Platform API",
    description="Backend API for the Customer Success TTV Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Customer Success TTV Platform API is running!"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }