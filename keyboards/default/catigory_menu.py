from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

catigory = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text = "Phones"),
           KeyboardButton(text = "Laptop"),
            
        ],
        [
           KeyboardButton(text = "Devices"),
           KeyboardButton(text = "PC"),
            
        ],
        [
           KeyboardButton(text = "Devices"),
           KeyboardButton(text = "PC"), 
        ],
    ],
    resize_keyboard=True
)