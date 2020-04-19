from backend.project import Project
import pytest


@pytest.fixture
def default_project():
    return Project()


def test_default_project(default_project):
    assert len(default_project.plays) == 0
