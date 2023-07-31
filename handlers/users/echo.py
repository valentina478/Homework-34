from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

@dp.message_handler()
async def task1(message: types.Message):
    if message.text.lower() == 'доброго ранку':
        await message.answer('Доброго ранку, чим будеш снідати?')
        await message.answer_sticker(f'CAACAgQAAxkBAAMDZLOVQ25WJgqQuvqkFfYjp8vzpL0AAooAA845CA0kZxLeXqKrGy8E')


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def bot_send_sticker(message: types.Message):
    await message.answer(f"Info about sticker\n animation - {message.sticker.is_animated}\n size - {message.sticker.file_size}")
    await message.answer_sticker(f"{message.sticker.file_id}")


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Ехо без стану."
                         f"Повідомлення:\n"
                         f"{message.text}")


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Ехо в стані <code>{state}</code>.\n"
                         f"\nЗміст повідомлення:\n"
                         f"<code>{message}</code>")
