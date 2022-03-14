from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_language = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "🇺🇿 O'zbekcha"),
           KeyboardButton(text = "🇷🇺 Русский"),
            
        ],
    ],
    resize_keyboard=True
)