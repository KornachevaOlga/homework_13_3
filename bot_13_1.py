from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

# @dp.message_handler(text = ['Хочу бота', 'Сколько стоит бот'])
# async def user_message(message):
#     print('Хочу бота message')
#     print('Сколько стоит бот message')
#
# @dp.message_handler(commands=['start'])
# async def start_message(message):
#     print('Start message')
    #await message.answer('Мы рады вас видеть в нашем чате!')
#
# @dp.message_handler()
# async def all_message(message):
#     print('Мы получили сообщение')

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью. message')
    await message.answer('Привет! Я бот помогающий твоему здоровью!')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(message.text.upper())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
