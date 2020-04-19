from backend.app import App
import pytest


@pytest.fixture
def default_app():
    return App()


def test_app_initialization(default_app):
    assert len(default_app.projects) == 0
