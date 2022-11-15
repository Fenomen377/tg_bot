from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from db import models
from db.models import BD1

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Перейти на сайт ресторана🇬🇪', url='http://212.192.31.65/')
urlkb.add(urlButton)


# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Забронировать стол"),
            types.KeyboardButton(text="Меню"),
            types.KeyboardButton(text="Контакты"),
            types.KeyboardButton(text='Режим работы'),
            types.KeyboardButton(text='Расположение'),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True).add(urlButton)

    await message.reply(f'Привет, {message.from_user.first_name}!👋 Я Гамарджоба-бот для бронирования столиков в ресторане ГамарджобаГенацвале🇬🇪', reply_markup=keyboard)


# @dp.message_handler()
async def commands(message: types.Message):
    if message.text == 'Контакты':
        await message.reply('Администратор: @kgf_kamil')
    elif message.text == 'Режим работы':
        await message.reply('Пн-Чт с 11:00 до 23:00, Пт-Вс с 11:00 до 00:00')
    elif message.text == 'Расположение':
        await message.reply('г. Москва, ул. Пушкина, д. Колотушкина 66')
    elif message.text == 'Перейти на сайт ресторана🇬🇪':
        await message.reply('Вы можете перейти на сайт ресторана по ссылке: 212.192.31.65')
    elif message.text == 'Меню':
        await message.reply(BD1.psql_read())
    elif message.text == 'Блюда из печи':
        await message.reply(BD1.psql_read_napitki())


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(commands)