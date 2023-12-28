from aiogram import Bot , Dispatcher , types
from aiogram.filters.command import Command
import asyncio
import logging
from my_token_bot import my_token
import requests



response = requests.get('https://ubilling.net.ua/aerialalerts/')
data = response.json()

bot = Bot(token=my_token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message:types.Message):
    await message.answer("hi")

@dp.message(Command('regions'))
async def regions_command(message:types.Message):
    await message.answer('''Виберете регион :
                         Киевская область - /kievregion
                         Луганская область - /lugansk''')

@dp.message(Command('kievregion'))
async def kievregion_command(message:types.Message):
    kiyiv_status = data['states']['Київська область']['alertnow']

    if kiyiv_status:
        await message.answer("Внимание! В Киевской области воздушная тревога ! ")
    else:
        await message.answer("В Киевской области нету тревоги , все спокойно ")

@dp.message(Command('lugansk'))
async def lugansk_command(message:types.Message):
    lugansk_status = data['states']['Луганська область']['alertnow']

    if lugansk_status:
        await message.answer("Внимание! В Луганской области воздушная тревога ! ")
    else:
        await message.answer("В Луганской области нету тревоги , все спокойно ")
    

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Bot started')
    
    
    

    asyncio.run(main())
  
 

