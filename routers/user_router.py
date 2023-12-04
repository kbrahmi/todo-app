from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
async def read_users():
    return {"users": ["user 1", "user 2"]}