"""Routes."""
import datetime

from sanic.response import json


def jsonify(records):
    """Parse asyncpg record response into JSON format."""
    json_arr = []
    for row in records:
        json_dict = {}
        for key in row.keys():
            if isinstance(row[key], datetime.datetime):
                json_dict[key] = row[key].timestamp()
            else:
                json_dict[key] = row[key]
        json_arr.append(json_dict)
    return json_arr


def setup_routes(app):
    """Routes setup."""

    @app.route("/")
    async def index(request):
        return json({"hello": "world"})

    @app.get("/api/posts")
    async def api_posts(request):
        async with app.pool.acquire() as connection:
            results = await connection.fetch("SELECT * FROM sanic_post")
            # ujson 2.x+ doesn't support serialising datetime.datetime
            # dump using standard json instead
            return json({"posts": jsonify(results)})
