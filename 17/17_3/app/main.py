from fastapi import FastAPI
import uvicorn

# from task import task_router
# from user import user_router
# app = FastAPI()
# app.include_router(task_router, prefix="/task")
# app.include_router(user_router, prefix="/user")

from routers import user, task
app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.task_router)
app.include_router(user.user_router)

'''  pip install alembic  
   alembic init app/migrations
добавить в env :
from app.backend.db import Base
from app.models.task import Task
from app.models.user import User
изменить:
target_metadata = Base.metadata
в alembic.ini изменить:
sqlalchemy.url = sqlite:///taskmanager.db
   
   alembic revision --autogenerate -m "Initial migration"  '''

# python -m uvicorn main:app


