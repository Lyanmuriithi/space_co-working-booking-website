from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class CoWorkingSpaceBase(BaseModel):
    name: str
    location: str
    description: Optional[str] = None
    price_per_hour: float

class CoWorkingSpaceCreate(CoWorkingSpaceBase):
    pass

class CoWorkingSpace(CoWorkingSpaceBase):
    id: int

    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    user_id: int
    co_working_space_id: int
    start_time: datetime
    end_time: datetime
    total_amount: float

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    booking_id: int
    amount: float
    payment_method: str

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True
