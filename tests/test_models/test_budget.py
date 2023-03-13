"""
Тесты для модели бюджета
"""
from datetime import datetime

import pytest

from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.models.budget import Budget


@pytest.fixture
def repo():
    return MemoryRepository()


def test_create_with_full_args_list():
    b = Budget(period="day", category=1, limitation=500, pk=1)
    assert b.period == "day"
    assert b.category == 1
    assert b.limitation == 500


def test_create_brief():
    b = Budget("day", 1, 500)
    assert b.period == "day"
    assert b.category == 1
    assert b.limitation == 500


def test_can_add_to_repo(repo):
    b = Budget("day", 1, 500)
    pk = repo.add(b)
    assert b.pk == pk
