from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('دعم💊', url='t.me/ooonn2'),
            InlineKeyboardButton('مطور👨‍💻', url='t.me/ooonn2')
        ]
        ]

close = [
        [
            InlineKeyboardButton('دعم💊', url='t.me/ooonn2'),
            InlineKeyboardButton('❌اغلق ❌', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
