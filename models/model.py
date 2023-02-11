from pydantic import BaseModel
from typing import Optional


class CustomerInfo(BaseModel):
    name: str
    email: str
    address: Optional[str] = ""
    national_id: str


class BookingInfo(BaseModel):
    vehicle_id: int
    hire_date: str
    return_date: str
    is_paid: bool


class BookingRequest(BaseModel):
    booking_info: BookingInfo
    customer_info: CustomerInfo
