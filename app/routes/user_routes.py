from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin, UserProfile
from fastapi_jwt_auth import AuthJWT
from passlib.hash import bcrypt

router = APIRouter()

@router.post("/users/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed = bcrypt.hash(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "User registered"}

@router.post("/users/login/")
def login(user: UserLogin, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = Authorize.create_access_token(subject=db_user.id)
    return {"access_token": access_token}

@router.get("/users/profile/", response_model=UserProfile)
def profile(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    user_id = Authorize.get_jwt_subject()
    user = db.query(User).get(user_id)
    return user

@router.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/users/logout/")
def logout():
    return {"msg": "Logout endpoint (client-side token discard recommended)"}
