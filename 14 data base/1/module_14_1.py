import random
import sqlite3

connection = sqlite3.connect("not_telegram.db") # обращение к файлу (базе данных)  
cursor = connection.cursor()  # инструмент по взаимодействию с таблицей данных

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXTNOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

################################################################################################
for i in range(10):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",  # Создание базы
                   (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

###############################################################################################

cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500, )) # Изменение

#################################################################################################


cursor.execute("DELETE FROM Users WHERE (id - 1) % 3 == 0") # Удаление


connection.commit()  # коммит - сохранение состояния
connection.close()  # закрытие соединения