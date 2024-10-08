from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin") # на одинаковый запрос будет выбираться первый декоратор
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user_info(username: str, age: int) -> dict: # можно задать ожидаемые параметры запроса, а также сами age=23
    return {"message": f"Информация о пользователе. Имя: {username} Возраст : {age}"}


# python -m uvicorn module_16_1:app