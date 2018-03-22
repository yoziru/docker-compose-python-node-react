from asyncpg import create_pool
from sanic import Sanic
from sanic.response import json


def jsonify(records):
    """
    Parse asyncpg record response into JSON format
    """
    return [dict(r.items()) for r in records]


app = Sanic()
DB_CONFIG = {
    'user': 'postgres',
    'password': '',
    'host': 'db',
    'port': 5432,
    'database': 'postgres'
}


@app.listener('before_server_start')
async def register_db(app, loop):
    app.pool = await create_pool(**DB_CONFIG, loop=loop, max_size=100)
    async with app.pool.acquire() as connection:
        await connection.execute('DROP TABLE IF EXISTS sanic_post')
        await connection.execute("""CREATE TABLE sanic_post (
                                id serial primary key,
                                content varchar(64),
                                post_date timestamp
                            );""")
        for i in range(0, 5):
            content = f'Hello from Sanic - {i}'
            await connection.execute(f"""INSERT INTO sanic_post(id, content, post_date)
            VALUES ({i}, '{content}', now())""")


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.get('/api/posts')
async def root_get(request):
    async with app.pool.acquire() as connection:
        results = await connection.fetch('SELECT * FROM sanic_post')
        return json({'posts': jsonify(results)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
