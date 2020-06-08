"""Sanic server."""
import os

from asyncpg import create_pool
from sanic import Sanic
from sanic.log import logger
from sanic_cors import CORS

from .middlewares import setup_middlewares
from .routes import setup_routes

DB_CONFIG = {
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", "password"),
    "host": os.getenv("POSTGRES_HOST", "db"),
    "port": int(os.getenv("POSTGRES_PORT", 5432)),
    "database": os.getenv("POSTGRES_DB", "postgres"),
}


def init_app():
    """Initialise Sanic app."""
    logger.debug("Initialising Sanic..")
    app = Sanic(name="backend-api")
    logger.debug("Adding CORS..")
    CORS(app, automatic_options=True)
    logger.debug("Setting up routes..")
    setup_routes(app)
    logger.debug("Setting up middlewares..")
    setup_middlewares(app)

    @app.listener("before_server_start")
    async def register_db(app, loop):
        app.pool = await create_pool(**DB_CONFIG, loop=loop, max_size=100)
        async with app.pool.acquire() as connection:
            await connection.execute("DROP TABLE IF EXISTS sanic_post")
            await connection.execute(
                """CREATE TABLE sanic_post (
                                    id serial primary key,
                                    content varchar(64),
                                    post_date timestamp
                                );"""
            )
            for i in range(0, 5):
                content = f"Hello from Sanic - {i}"
                await connection.execute(
                    f"""INSERT INTO sanic_post(id, content, post_date)
                VALUES ({i}, '{content}', now())"""
                )

    return app


if __name__ == "__main__":
    app = init_app()
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        auto_reload=os.getenv("SANIC_AUTORELOAD", False),
    )
