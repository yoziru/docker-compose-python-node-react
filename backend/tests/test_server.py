import pytest

from src.server import init_app

app = init_app()


@pytest.fixture(scope="module")
def test_response_index():
    _, response = app.test_client.get("/")
    return response


def test_index_status_ok(test_response_index):
    assert test_response_index.status == 200


@pytest.fixture(scope="module")
def test_response_posts():
    _, response = app.test_client.get("/api/posts")
    return response


def test_posts_status_ok(test_response_posts):
    assert test_response_posts.status == 200


def test_posts_return_dict(test_response_posts):
    assert isinstance(test_response_posts.json, dict)
