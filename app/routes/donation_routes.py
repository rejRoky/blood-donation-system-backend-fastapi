from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_donations():
    return {"message": "All donations listed here"}
