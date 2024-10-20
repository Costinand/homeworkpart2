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

# python -m uvicorn main:app
