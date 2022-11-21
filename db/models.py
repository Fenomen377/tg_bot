import psycopg2 as psycopg2
from aiogram.types import ReplyKeyboardMarkup
from decouple import config

from create_bot import bot

con = psycopg2.connect(dbname=config('dbname'), user=config('user'), password=config('password'), host=config('host'),
                       port=config('port'))
cur = con.cursor()


def psql_read_desert():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=142')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🧁' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_napitki():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=10')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🥤' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_hinkali():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=9')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🥟' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_sous():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=8')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🥫' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_garnir():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=7')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🍝' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_soup():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=6')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🍜' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_zakuski():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=5')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🍢' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_mangal():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=4')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🥩' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_goryachee():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=3')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🍲' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_salati():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=2')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🥗' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read_pechka():
    cur.execute('SELECT name, description, price, weight FROM menu_menu WHERE category_id=1')
    query_results = cur.fetchall()
    for row in query_results:
        text = '\n'.join([f''.join(map(str, '\n' + '🥮' + str(x[0]) + '\nОписание: ' + str(x[1]) + '\nЦена: ' + str(
            x[2]) + '₽ | ' + str(x[3]))) + 'г.' for x in query_results])
        return str(text)


def psql_read():
    cur.execute('SELECT name FROM menu_category')
    query_results = cur.fetchall()
    text = '🧾Категории меню:' + '\n—' + '\n—'.join([', '.join(map(str, x)) for x in query_results])
    return str(text)


cur.execute('''
CREATE TABLE IF NOT EXISTS Типы (
    id SERIAL PRIMARY KEY,
    Тип TEXT);

''')
con.commit()


cur.execute('''
CREATE TABLE IF NOT EXISTS Столики (
    id SERIAL PRIMARY KEY,
    Столик INTEGER NOT NULL,
    Тип INT NOT NULL,
    FOREIGN KEY(Тип) REFERENCES Типы,
    place INTEGER NOT NULL);

''')
con.commit()


cur.execute('''
CREATE TABLE IF NOT EXISTS Бронирование (
    id SERIAL PRIMARY KEY,
    Столик INTEGER,
    Дата DATE NOT NULL,
    FOREIGN KEY(Столик) REFERENCES Столики(id),
    CONSTRAINT Бронь UNIQUE (Столик, Дата));
''')
con.commit()


def table_read():
    cur.execute('SELECT * FROM Типы')
    query_results = cur.fetchall()
    text = 'В каком зале вы хотите забронировать стол?'
    return str(text)

# 🗓На какое число желаете забронировать стол?\nВведите дату в формате YYYY-MM-DD


def table_VIP():
    cur.execute('SELECT Столик, place FROM Столики WHERE Тип=1')
    query_results = cur.fetchall()
    for row in query_results:
        text = '⚜VIP-зал⚜\n\n🛑Выберите стол для бронирования🛑\n'+'\n'.join([f''.join(map(str, '\n' + 'VIP-зал №' + str(x[0]) + ' | ' + 'Количество мест: ' + str(x[1]))) for x in query_results])
        return str(text)


def table_mer():
    cur.execute('SELECT Столик, place FROM Столики WHERE Тип=2')
    query_results = cur.fetchall()
    for row in query_results:
        text = 'Зал мероприятий\n\n🛑Выберите стол для бронирования🛑\n'+'\n'.join([f''.join(map(str, '\n' + 'Столик №' + str(x[0]) + ' | ' + 'Количество мест: ' + str(x[1]))) for x in query_results])
        return str(text)


def table_ver():
    cur.execute('SELECT Столик, place FROM Столики WHERE Тип=3')
    query_results = cur.fetchall()
    for row in query_results:
        text = 'Веранда\n\n🛑Выберите стол для бронирования🛑\n'+'\n'.join([f''.join(map(str, '\n' + 'Столик №' + str(x[0]) + ' | ' + 'Количество мест: ' + str(x[1]))) for x in query_results])
        return str(text)


def table_1():
    cur.execute('SELECT Столик, place FROM Столики WHERE Тип=4')
    query_results = cur.fetchall()
    for row in query_results:
        text = 'Зал №1\n\n🛑Выберите стол для бронирования🛑\n'+'\n'.join([f''.join(map(str, '\n' + 'Столик №' + str(x[0]) + ' | ' + 'Количество мест: ' + str(x[1]))) for x in query_results])
        return str(text)


def table_2():
    cur.execute('SELECT Столик, place FROM Столики WHERE Тип=5')
    query_results = cur.fetchall()
    for row in query_results:
        text = 'Зал №2\n\n🛑Выберите стол для бронирования🛑\n'+'\n'.join([f''.join(map(str, '\n' + 'Столик №' + str(x[0]) + ' | ' + 'Количество мест: ' + str(x[1]))) for x in query_results])
        return str(text)


def table_3():
    cur.execute('SELECT Столик, place FROM Столики WHERE Тип=6')
    query_results = cur.fetchall()
    for row in query_results:
        text = 'Зал №3\n\n🛑Выберите стол для бронирования🛑\n'+'\n'.join([f''.join(map(str, '\n' + 'Столик №' + str(x[0]) + ' | ' + 'Количество мест: ' + str(x[1]))) for x in query_results])
        return str(text)
