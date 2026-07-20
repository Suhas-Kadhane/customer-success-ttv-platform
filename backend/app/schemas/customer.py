from pydantic import BaseModel


class CustomerCreate(BaseModel):
    company_name: str
    industry: str

class CustomerResponse(BaseModel):
    id: int
    company_name: str
    industry: str
    status: str

    class Config:
        from_attributes = True