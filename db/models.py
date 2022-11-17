import psycopg2 as psycopg2
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
