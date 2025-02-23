import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
from app.api.device_info import router as device_information_router
# from app.api.v1.device_status import router as device_status_router
load_dotenv()
app = FastAPI(
    title="Device Information",
    description="Simple API using FastAPI for gathering information about android device using ADB",
    version="1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(device_information_router, prefix="/v1", tags=["device"])

@app.get("/", include_in_schema=False)
async def root_redirect():
    return RedirectResponse(url="/docs")