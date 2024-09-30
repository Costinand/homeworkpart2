from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions import *

api = "" # для авторизации используется токен(номер и пароль в одном)
bot = Bot(token=api)  #  создание бота с единственным параметром (API протокол взаимодействия с другими приложениями)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True) # Создаем клавиатуру. в параметре подгон под размер экрана
button = KeyboardButton(text= "Информация") # Создание клавиш
button2 = KeyboardButton(text= "Рассчитать")
button3 = KeyboardButton(text="Купить")
kb.row(button, button2)  # Добавление клавиш
kb.add(button3)

kb2 = InlineKeyboardMarkup(row_width= 2) # в парамете указано склько кнопок в ряду
button21 = InlineKeyboardButton(text= "Формула расчета", callback_data= 'formulas')
button22 = InlineKeyboardButton(text= "Рассчитать норму калорий", callback_data= 'calories')
kb2.add(button21, button22)

kb3 = InlineKeyboardMarkup(row_width= 4)
button31 = InlineKeyboardButton(text= "Product 1", callback_data= 'product_buying')
button32 = InlineKeyboardButton(text= "Product 2", callback_data= 'product_buying')
button33 = InlineKeyboardButton(text= "Product 3", callback_data= 'product_buying')
button34 = InlineKeyboardButton(text= "Product 4", callback_data= 'product_buying')
kb3.add(button31, button32, button33, button34)


photos = ["1.png", "2.png", "3.png", "4.png"]
products = get_all_products() # cодержимое аблицы ввиде списка
p_list = [item for sublist in products for item in sublist] # делаю сплошной список для свободного индексирования
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup = kb)



@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Скоро здесь появится информация')

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = kb2)

@dp.message_handler(text= "Купить")
async def get_buy_list(message):
    for i in range(4):
        with open(f'photos/{photos[i]}', "rb") as img: # индексированеие по принципу: у каждого продукта 4 характеристики
            if i == 0:  # значит чтобы перемещаться по проодуктам нужно умножать i на четыре. тут отработка ноля
                await message.answer_photo(img, f"Название: {p_list[i + 1]} | Описание: {p_list[i+2]} | Цена: {p_list[i+3]}")
            else:
                await message.answer_photo(img, f"Название: {p_list[i*4 + 1]} | Описание: {p_list[i*4+2]} | Цена: {p_list[i*4+3]}")
    await message.answer("Выберите продукт:", reply_markup = kb3)

@dp.callback_query_handler(text = ['product_buying'])
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    # await call.answer  # закомментировал, потому что выдает о неизвестном методе. Бот при этом продолжает работать
                                                                                     # и с ней и без неё

@dp.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    """10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 мужчины"""
    norm = int(data['third']) * 10 + int(data['second']) * 6.25 - int(data['first']) * 5 + 5
    await message.answer(f"Ваша норма калорий {norm}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)