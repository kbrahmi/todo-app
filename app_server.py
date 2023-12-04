from fastapi import FastAPI, responses
from routers import user_router

app = FastAPI()

app.include_router(user_router.router)

@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse("/docs")