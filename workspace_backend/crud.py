from sqlalchemy.orm import Session
from models import User as UserModel
from schemas import UserCreate, User

def create_user(db: Session, username: str, email: str, hashed_password: str):
    db_user = UserModel(username=username, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserModel).offset(skip).limit(limit).all()
