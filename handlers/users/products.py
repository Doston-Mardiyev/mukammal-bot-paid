from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.phone_catigorys import catigory_of_phones
from loader import dp



@dp.message_handler(text = "Phones")
async def show_menu_uz(message: Message):
    await message.answer("Phones menu", reply_markup = catigory_of_phones)