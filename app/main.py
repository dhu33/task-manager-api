from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from app.routers.task import router as tasks_router
app=FastAPI()
app.include_router(tasks_router)
# My first GitHub update
# Working on add_auth branch