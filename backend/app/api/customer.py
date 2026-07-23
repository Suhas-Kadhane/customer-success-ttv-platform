from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerResponse

router = APIRouter()


@router.post("/customers", response_model=CustomerResponse)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    db_customer = Customer(
        company_name=customer.company_name,
        industry=customer.industry
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


@router.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.get("/customers", response_model=List[CustomerResponse])
def get_all_customers(
    db: Session = Depends(get_db)
):
    customers = db.query(Customer).all()

    return customers


@router.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if db_customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db_customer.company_name = customer.company_name
    db_customer.industry = customer.industry

    db.commit()
    db.refresh(db_customer)

    return db_customer


@router.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if db_customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(db_customer)
    db.commit()

    return {
        "message": "Customer deleted successfully"
    }