"""
Тесты для модели бюджета
"""
from datetime import datetime, timedelta

import pytest

from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.models.budget import Budget
from bookkeeper.models.expense import Expense


@pytest.fixture
def repo():
    return MemoryRepository()


def test_create_with_full_args_list():
    b = Budget(period="day", total=100, limitation=500, pk=1)
    assert b.period == "day"
    assert b.total == 100
    assert b.limitation == 500


def test_create_brief():
    b = Budget("day", 100, 500)
    assert b.period == "day"
    assert b.total == 100
    assert b.limitation == 500


def test_can_add_to_repo(repo):
    b = Budget("day", 100, 500)
    pk = repo.add(b)
    assert b.pk == pk


def test_update_sum(repo):
    date = datetime.now()
    e1 = Expense(100, 1, expense_date=date.isoformat()[:10])
    e2 = Expense(100, 1, expense_date=(date - timedelta(days=5)).isoformat()[:10])
    e3 = Expense(100, 1, expense_date=(date - timedelta(days=10)).isoformat()[:10])
    repo.add(e1)
    repo.add(e2)
    repo.add(e3)
    # day
    b1 = Budget("day", 0, 500)
    b1.update_total(repo)
    assert b1.total == 100
    # week
    b2 = Budget("week", 0, 500)
    b2.update_total(repo)
    assert b2.total == 200
    # month
    b3 = Budget("month", 0, 500)
    b3.update_total(repo)
    assert b3.total == 300


def test_wrong_period():
    with pytest.raises(ValueError):
        Budget(period="year", total=100, limitation=500)