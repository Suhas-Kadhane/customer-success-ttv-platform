from fastapi import FastAPI

from app.api.customer import router as customer_router
from app.core.database import Base, engine
from app.models.customer import Customer

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Customer Success TTV Platform API",
    description="Backend API for the Customer Success TTV Platform",
    version="1.0.0"
)

app.include_router(customer_router)

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