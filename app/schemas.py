from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserProfile(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_first_donation: bool
    class Config:
        orm_mode = True

class DistrictOut(BaseModel):
    id: int
    name: str

class UpazilaOut(BaseModel):
    id: int
    name: str
    district_id: int

class DonationRequest(BaseModel):
    status: str

