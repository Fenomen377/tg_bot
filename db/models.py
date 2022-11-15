import psycopg2 as psycopg2
from decouple import config

from create_bot import bot


con = psycopg2.connect(dbname=config('dbname'), user=config('user'), password=config('password'), host=config('host'), port=config('port'))
cur = con.cursor()


class BD1:

    def psql_read():
        cur.execute('SELECT name FROM menu_category')
        query_results = cur.fetchall()
        text = 'Категории меню:'+'\n\n✅'+'\n\n✅'.join([', '.join(map(str, x)) for x in query_results])
        return (str(text))

    def psql_read_napitki():
        cur.execute('SELECT name, description, photo, price, weight FROM menu_menu WHERE category_id=1')
        query_results = cur.fetchall()
        text = 'Блюда из печи:' + '\n\n✅' + '\n\n✅'.join([f'\n'.join(map(str, x)) for x in query_results])
        return (str(text))

