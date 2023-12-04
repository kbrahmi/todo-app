from fastapi import APIRouter
# from managers.task_management import TaskManager


router = APIRouter()
# manager = TaskManager()


@router.get("/")
async def read_tasks():
    return # manager.get_all_tasks()


@router.get("/{task_id}")
async def read_task(task_id: int):
    return # manager.get_task_by_id(task_id)


@router.post("/")
async def create_task(task):
    return # manager.create_task(task)


@router.patch("/{task_id}")
async def update_task(task_id: int, task):
    return # manager.update_task(task_id, task)


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    return # manager.delete_task(task_id)
