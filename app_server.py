from fastapi import FastAPI, responses, Depends
from authentication.token import create_access_token, get_current_user
from routers import user_router
from routers import task_router
from routers import login_router
from database import init_db
from authentication.token import oauth2_scheme


app = FastAPI()

init_db()

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(task_router.router, prefix="/tasks", tags=["tasks"])
app.include_router(login_router.router, prefix="/login", tags=["login"])


@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse("/docs")


# @app.post("/token")
# async def login_for_access_token():
#    access_token = create_access_token(data={"sub": "username"})
#    return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/users/me")
# async def read_users_me(current_user: dict = Depends(get_current_user)):
#    return current_user
