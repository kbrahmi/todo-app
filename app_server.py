from fastapi import FastAPI, responses

from routers import user_router
from routers import task_router
from database import init_db


app = FastAPI()

init_db()

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(task_router.router, prefix="/tasks", tags=["tasks"])


@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse("/docs")
