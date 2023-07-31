from aiogram import types

from loader import dp

@dp.message_handler(commands=['info'])
async def bot_say_info(message: types.Message):
    await message.answer(f"{message.from_user.full_name} - your language {message.from_user.language_code}")

@dp.message_handler(commands=['saysomething'])
async def task2(message: types.Message):
    await message.answer(text= 'Чи відомі вам людські ліні №212682340236: \nВи надто ліниві, щоб прочитати це число.')