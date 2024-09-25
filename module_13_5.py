from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "" # для авторизации используется токен(номер и пароль в одном)
bot = Bot(token=api)  #  в этом нужно разобраться
dp = Dispatcher(bot, storage=MemoryStorage()) # мой диспатчер наследует из пакета

kb = ReplyKeyboardMarkup(resize_keyboard=True) # Создаем клавиатуру
button = KeyboardButton(text= "Информация") # Создание клавиш
button2 = KeyboardButton(text= "Рассчитать")
kb.row(button, button2)  # Добавление клавиш

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

@dp.message_handler(text = "Рассчитать")
async def set_age(message):
    await message.answer('Введите свой возраст:')
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


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



