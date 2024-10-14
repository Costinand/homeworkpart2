from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async  def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}") # Добавление пользователя
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> dict:

    user_id = str(int(max(users, key=int)) + 1) # номер пользователя
    data = f"Имя: {username}, возраст: {age}" # содержимое строки пользователя
    users[user_id] = data # добавление в базу  users данных
    return {f"User {user_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}") # Изменение содержимого ячейки
async def update_users(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")],
        user_id: int = Path(ge=0)) -> dict:

    users[user_id] = f"Имя: {username}, возраст: {age}" # изменение ячейки номер user_id
    return {"message": f"The user {user_id} is updated"}

@app.delete("/user/{user_id}") # Удаление ячейки
async def delete_users(user_id: str) -> str:
    users.pop(user_id)
    return {"message": f"User {user_id} has been deleted."}

#    python -m uvicorn module_16_3:app