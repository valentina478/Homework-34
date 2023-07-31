from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Button 1', callback_data='second'),
        ]
    ]
)


button_exit = InlineKeyboardButton('Exit', callback_data='exit')
button_call_manager = InlineKeyboardButton('Call manager', callback_data='call_manager')
button_test = InlineKeyboardButton('test', callback_data='test')


first.add(button_exit)
first.add(button_call_manager)

row_keyboard = InlineKeyboardMarkup().row(button_exit, button_call_manager, button_test)
button4 = InlineKeyboardButton('4', callback_data='4')
button5 = InlineKeyboardButton('5', callback_data='5')


markup3 = InlineKeyboardMarkup()

markup3.row(button_exit, button_call_manager, button_test)
markup3.add(InlineKeyboardButton('Big brother', callback_data='1'))
markup3.row(button4, button5)

social = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Youtube", url='https://www.youtube.com/'), InlineKeyboardButton("Twitch", url='https://www.twitch.com/')],
        [InlineKeyboardButton("LinkdIn", url='https://www.linkedin.com/'), ],
        [InlineKeyboardButton("Twitter", url='https://x.com/'), ],
    ]
)

songs = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Runaway — AURORA', url='https://open.spotify.com/track/1v1oIWf2Xgh54kIWuKsDf6?si=12c2dc94bc9f45c7)')],
        [InlineKeyboardButton('Кожен новий день — Epolets', url='https://open.spotify.com/track/46Z8QzcjdCxqaiHeK78fnU?si=68b58b418a68418a')]
    ]
)

films = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Дівчина ХХ століття', url='https://uakino.club/filmy/genre_melodrama/16807-dvchina-xx-stolttya.html'), InlineKeyboardButton('Тихе місце', url='https://uakino.club/filmy/genre_drama/7103-tihe-msce.html')]
    ]
)