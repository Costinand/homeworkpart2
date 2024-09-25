from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "" # для авторизации используется токен(номер и пароль в одном)
bot = Bot(token=api)  #  в этом нужно разобраться
dp = Dispatcher(bot, storage=MemoryStorage()) # мой диспатчер наследует из пакета

@dp.message_handler(text = ['Urban', 'ff']) # этот реагирует на определенный текст
async def urban_message(message):
    print("Urban_message")

@dp.message_handler(commands=['start'])  # этот реагирует на определенные команды(идут после слэша \ )
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()  # Хандлер - обработчик(принимает и выполняет) по сути декоратор
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)