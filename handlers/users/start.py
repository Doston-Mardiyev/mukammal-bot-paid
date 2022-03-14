from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.language import menu_language
from keyboards.default.menu_keyboard import menu_ru, menu_uz
from keyboards.default.catigory_menu import catigory
from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: Message):
    await message.answer("Intraduction about market", reply_markup=menu_language)

@dp.message_handler(text = "🇺🇿 O'zbekcha")
async def show_menu_uz(message: Message):
    await message.answer("Asosiy menyu", reply_markup = menu_uz)

@dp.message_handler(text = "🏠 Mahsulotlar")
async def show_products(message: Message):
    await message.answer("Mahsulotlat", reply_markup = catigory)


@dp.message_handler(text = "🇷🇺 Русский")
async def show_menu_ru(message: Message):
    await message.answer("Главное меню", reply_markup = menu_ru)