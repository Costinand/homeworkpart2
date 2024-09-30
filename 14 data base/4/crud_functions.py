import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()

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

    for i in range(1,5):
        cursor.execute("INSERT INTO Products(title, descrition, price) VALUES (?, ?, ?)",  # Создание базы
                       (f"Product {i}", discriptions[i-1] , i * 100))

    await message.answer_photo(img, f'Product {i} | Описание: описание {i} | Цена: {i * 100}')
    connection.commit()
def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products


initiate_db()


# connection.commit()  # коммит - сохранение состояния
# connection.close()  # закрытие соединения

