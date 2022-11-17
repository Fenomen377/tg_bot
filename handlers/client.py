from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from db import models
from db.models import *

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

    await message.reply(f'Привет, {message.from_user.first_name}!👋 Я Гамарджоба-бот для бронирования столиков в '
                        f'ресторане ГамарджобаГенацвале🇬🇪', reply_markup=keyboard)


# @dp.message_handler()
async def commands(message: types.Message):
    kbs =[
        [
            types.KeyboardButton(text='Блюда из печи'),
            types.KeyboardButton(text='Салаты'),
            types.KeyboardButton(text='Горячие блюда'),
        ],
    ]
    but1 = KeyboardButton(text='Супы')
    but2 = KeyboardButton(text='Гарниры')
    but3 = KeyboardButton(text='Соусы')
    but4 = KeyboardButton(text='Хинкали')
    but5 = KeyboardButton(text='Напитки')
    but6 = KeyboardButton(text='Десерты')
    but7 = KeyboardButton(text='Блюда на мангале')
    but8 = KeyboardButton(text='Закуски')
    but9 = KeyboardButton(text='/start')
    keyboard = types.ReplyKeyboardMarkup(keyboard=kbs, resize_keyboard=True).add(but7, but8, but1, but2, but3, but4, but5, but6, but9)
    if message.text == 'Контакты':
        await message.reply('Администратор: @kgf_kamil')
    elif message.text == 'Режим работы':
        await message.reply('Пн-Чт с 11:00 до 23:00, Пт-Вс с 11:00 до 00:00')
    elif message.text == 'Расположение':
        await message.reply('г. Москва, ул. Пушкина, д. Колотушкина 66')
    elif message.text == 'Перейти на сайт ресторана🇬🇪':
        await message.reply('Вы можете перейти на сайт ресторана по ссылке: gamarjoba.sytes.net')
    elif message.text == 'Забронировать стол':
        await message.reply('🗓Когда планируете посетить наш ресторан?\nВведите дату в формате YYYY-MM-DD')
    elif message.text == 'Меню':
        await message.reply(psql_read(), reply_markup=keyboard)
    elif message.text == 'Блюда из печи':
        await message.reply(psql_read_pechka())
    elif message.text == 'Салаты':
        await message.reply(psql_read_salati())
    elif message.text == 'Горячие блюда':
        await message.reply(psql_read_goryachee())
    elif message.text == 'Блюда на мангале':
        await message.reply(psql_read_mangal())
    elif message.text == 'Закуски':
        await message.reply(psql_read_zakuski())
    elif message.text == 'Супы':
        await message.reply(psql_read_soup())
    elif message.text == 'Гарниры':
        await message.reply(psql_read_garnir())
    elif message.text == 'Соусы':
        await message.reply(psql_read_sous())
    elif message.text == 'Хинкали':
        await message.reply(psql_read_hinkali())
    elif message.text == 'Напитки':
        await message.reply(psql_read_napitki())
    elif message.text == 'Десерты':
        await message.reply(psql_read_desert())


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(commands)