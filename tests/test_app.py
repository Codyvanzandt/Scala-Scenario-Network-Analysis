from backend.app import App
from backend.project import Project
from collections import OrderedDict
import pytest


@pytest.fixture
def default_app():
    return App()


@pytest.fixture
def default_project():
    return Project("Project0")


def test_app_initialization(default_app):
    # Projects
    assert isinstance(default_app.projects, OrderedDict)
    assert len(default_app.projects) == 0


def test_repr(default_app):
    assert repr(default_app) == f"App()"


def test_contains(default_app, default_project):
    # Case 1: does not contain
    assert default_project not in default_app
    assert default_project.title not in default_app

    # Case 2: does conain
    default_app.add_project(default_project)
    assert default_project in default_app
    assert default_project.title in default_app


def test_add_project(default_app, default_project):
    # Case 1: non-extant project
    default_app.add_project(default_project)
    assert default_project in default_app

    # Case 2: extant project; should raise ValueError
    with pytest.raises(ValueError) as add_project_error:
        default_app.add_project(default_project)
    assert (
        str(add_project_error.value) == f"{default_project.title} already exists in App"
    )


def test_remove_project(default_app, default_project):
    default_app.add_project(default_project)

    # Case 1: extant project
    default_app.remove_project(default_project)
    assert default_project not in default_app

    # Case 2: non-extant project; should quietly fail
    default_app.remove_project(default_project)
