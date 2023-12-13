from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.task_schema import TaskList, TaskBase
from managers.task_management.task_manager import TaskManager
from repositories.task_repository import TaskRepository
from database import get_db

router = APIRouter()


@router.get("/", response_model=TaskList)
async def read_tasks(db: Session = Depends(get_db)):
    task_manager = TaskManager(TaskRepository(db))
    tasks = task_manager.get_all_tasks()
    return TaskList(tasks=[TaskBase.from_orm(task) for task in tasks])


@router.get("/{id}", response_model=TaskBase)
async def read_task(task_id: int, db: Session = Depends(get_db)):
    task_manager = TaskManager(TaskRepository(db))
    task = task_manager.get_task_by_id(task_id)
    return task


@router.post("/")
async def create_task(task):
    return # manager.create_task(task)


@router.patch("/{id}")
async def update_task(task_id: int, task):
    return # manager.update_task(task_id, task)


@router.delete("/{id}")
async def delete_task(task_id: int):
    return # manager.delete_task(task_id)
