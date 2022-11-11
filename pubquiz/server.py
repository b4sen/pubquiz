import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from .api import api_router

DIRNAME = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(DIRNAME, "web", "build")

app = FastAPI()
app.include_router(api_router)


@app.get("/")
async def index():
    return RedirectResponse(url="/index.html")


app.mount("/", StaticFiles(directory=static_dir))
