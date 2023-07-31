from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привіт, {message.from_user.full_name}!")


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Це ехо без стану від start")