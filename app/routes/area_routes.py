from fastapi import APIRouter, Depends
from app.models import District, Upazila
from app.schemas import DistrictOut, UpazilaOut
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/area/district/", response_model=list[DistrictOut])
def get_districts(db: Session = Depends(get_db)):
    return db.query(District).all()

@router.get("/area/upazila/", response_model=list[UpazilaOut])
def get_upazilas(db: Session = Depends(get_db)):
    return db.query(Upazila).all()
