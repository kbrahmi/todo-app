from fastapi import FastAPI
from api import app_server
import uvicorn
app = FastAPI(
    title="Aristote",
    debug=False,
    version="0.2.7",
    docs_url="/",
)

if __name__ == "__main__":
    uvicorn.run(
        "app_server",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )