from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_users():
    return {"users": ["user 1", "user 2"]}


@router.get("/{id}/tasks")
async def read_user_tasks(id: int):
    return
