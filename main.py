
from fastapi import FastAPI
from routers.home import router as home_router

app = FastAPI(
    title="Library Management System",
    version="0.1.0",
    description="LMS API built with FastAPI",
)

app.include_router(home_router)
