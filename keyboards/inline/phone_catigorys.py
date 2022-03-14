from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


catigory_of_phones = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text = "Apple", callback_data='Sotish'),
           InlineKeyboardButton(text = "Samsung", callback_data='Olish'),
            
        ],
        [
           InlineKeyboardButton(text = "Huawei", callback_data='Arendaga berish'),
           InlineKeyboardButton(text = "Honor", callback_data='Arendaga olish'),
            
        ],
        [
           InlineKeyboardButton(text = "Xiaomi", callback_data='Tez uy olish'),
           InlineKeyboardButton(text = "Realme", callback_data='Ishonchli boshqaruv'),
            
        ],
         [
           InlineKeyboardButton(text = "Vivo", callback_data='Auksion tashkilotchisi'),
           InlineKeyboardButton(text = "Remax", callback_data='Meros hujjatlarni tayyorlash'),
            
        ],

        [
           InlineKeyboardButton(text = "Novey", callback_data='Turar hujjatlarni tayyorlash'),
           InlineKeyboardButton(text = "BQ", callback_data='Turar hujjatlarni tayyorlash'),
        ],
    ],
   
)