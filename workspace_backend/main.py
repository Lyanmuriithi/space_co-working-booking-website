from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from schemas import User, UserCreate, CoWorkingSpace, CoWorkingSpaceCreate, Booking, BookingCreate, Payment, PaymentCreate
import crud

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return{"message":"Hello Lyan"}

# User endpoints
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, username=user.username, email=user.email, hashed_password=user.hashed_password)

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

# Co-working Space endpoints
@app.post("/co-working-spaces/", response_model=CoWorkingSpace)
def create_co_working_space(space: CoWorkingSpaceCreate, db: Session = Depends(get_db)):
    return crud.create_co_working_space(db=db, name=space.name, location=space.location, description=space.description, price_per_hour=space.price_per_hour)

@app.get("/co-working-spaces/{space_id}", response_model=CoWorkingSpace)
def read_co_working_space(space_id: int, db: Session = Depends(get_db)):
    space = crud.get_co_working_space(db=db, space_id=space_id)
    if space is None:
        raise HTTPException(status_code=404, detail="Co-working space not found")
    return space

@app.get("/co-working-spaces/", response_model=list[CoWorkingSpace])
def read_co_working_spaces(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_co_working_spaces(db=db, skip=skip, limit=limit)

# Booking endpoints
@app.post("/bookings/", response_model=Booking)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, user_id=booking.user_id, co_working_space_id=booking.co_working_space_id, start_time=booking.start_time, end_time=booking.end_time, total_amount=booking.total_amount)

@app.get("/bookings/{booking_id}", response_model=Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.get_booking(db=db, booking_id=booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.get("/bookings/", response_model=list[Booking])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_bookings(db=db, skip=skip, limit=limit)

# Payment endpoints
@app.post("/payments/", response_model=Payment)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db=db, booking_id=payment.booking_id, amount=payment.amount, payment_method=payment.payment_method)

@app.get("/payments/{payment_id}", response_model=Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = crud.get_payment(db=db, payment_id=payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.get("/payments/", response_model=list[Payment])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_payments(db=db, skip=skip, limit=limit)
