from fastapi import FastAPI, Path, status, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
async  def get_all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]):
    new_id = len(users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return {f"User {new_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}") # Изменение содержимого ячейки
async def update_users(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")],
        user_id: int = Path(ge=0)):
    try:
        edit_username = users[user_id]
        edit_username.username = username
        edit_age = users[user_id]
        edit_age.age = age
        return {"message": f"The user {user_id} is updated"}
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}") # Удаление ячейки
async def delete_users(user_id: int):
    try:
        users.pop(user_id)
        return {"message": f"User {user_id} has been deleted."}
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

'''Работа с ID  некорректная. Индексация проходит как по обычному списку и это уже нужно учитывать, а после первого 
удаления ID сдвигаются. 
Возможно, если сделать ID строкой (как имя), это исправит ситуацию, но делал все, как написано в задании. На будующее,
 думаю, лучше использовать готовые инструменты для работы с базами данных'''

#    python -m uvicorn module_16_4:app
