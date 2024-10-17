from fastapi import FastAPI, Path, status, HTTPException, Request
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
users = []
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/") # Вывод списка на вэб страницу
async  def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/users/{user_id}")
async  def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}")
async def add_user(request: Request,
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> HTMLResponse:
    new_id = len(users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    # return {f"User {new_id} is registered"}
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.put("/user/{user_id}/{username}/{age}") # Изменение содержимого ячейки
async def update_users(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")],
        user_id: int = Path(ge=0)):
    try:
        edit_username = users[user_id -1]
        edit_username.username = username
        edit_age = users[user_id -1]
        edit_age.age = age
        return {"message": f"The user {user_id} is updated"}
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}") # Удаление ячейки
async def delete_users(user_id: int):
    try:
        users.pop(user_id -1)
        return {"message": f"User {user_id} has been deleted."}
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

'''Работа с ID  некорректная. Если речь идет о редактировании пользователя, то индексируется правильно, но стоит удалить 
 одного пользователя и все, кто ниже по списку индексируются не по номеру ID, а по индексам списка '''

#    python -m uvicorn module_16_5:app
