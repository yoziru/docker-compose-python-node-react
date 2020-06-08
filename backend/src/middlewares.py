"""Middlewares."""
from secure import SecureHeaders

secure_headers = SecureHeaders()


def setup_middlewares(app):
    """Middleware setup."""

    @app.middleware("response")
    async def set_secure_headers(request, response):
        secure_headers.sanic(response)
