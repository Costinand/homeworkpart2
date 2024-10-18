from fastapi import FastAPI
import uvicorn


from routers import user, task
app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.task_router)
app.include_router(user.user_router)

# python -m uvicorn main:app
