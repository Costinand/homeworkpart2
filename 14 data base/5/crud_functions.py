import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()
connection2 = sqlite3.connect("Users.db")
cursor2 = connection2.cursor()

discriptions = ["Похудин.Чай (20 пак)", "Похудин.Компот(20 порц)", "Похудин.Драже(250 шт)", "Похудин.Капсулы(50 кап)"]

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    descrition TEXT,
    price INTEGER NOT NULL
    )
    ''')
    #
    # for i in range(1,5):
    #     cursor.execute("INSERT INTO Products(title, descrition, price) VALUES (?, ?, ?)",  # Создание базы
    #                    (f"Product {i}", discriptions[i-1] , i * 100))
    #
    # await message.answer_photo(img, f'Product {i} | Описание: описание {i} | Цена: {i * 100}')
    # connection.commit()

    cursor2.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

def add_user(username, email, age):
    # cursor2.execute(f'''
    # INSERT INTO Users VALUES('{username}','{email}', '{age}')
    # ''') # форма если все элементы динамические т.е. задаются каждый раз
    cursor2.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
     (username, email, age, 1000)) # форма заполнения, если есть элементы статические как balance

    connection2.commit()

def is_included(username):
    check_user = cursor2.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_user.fetchone() is None:
        connection2.commit()
        return False
    else:
        connection2.commit()
        return True



def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    return products


initiate_db()
# print(get_all_products())

# connection.commit()  # коммит - сохранение состояния
# connection.close()  # закрытие соединения

