"""
Модель бюджета
"""
from datetime import datetime, timedelta
from dataclasses import dataclass
from bookkeeper.models.expense import Expense
from bookkeeper.repository.abstract_repository import AbstractRepository


@dataclass
class Budget:
    """
    Бюджет, хранит срок рассмотрения в атрибуте period ("day", "week", "month"),
    потраченная сумма за рассматриваемый срок в атрибуте sum,
    лимит расходов на заданный срок в атрибуте limitation,
    """
    period: str
    total: int
    limitation: int
    pk: int = 0

    def __init__(self, period: str, total: int, limitation: int, pk: int = 0):
        if period not in ["day", "week", "month"]:
            raise ValueError(f'unknown period "{period}" '
                             + 'should be "day", "week" or "month"')
        self.period = period
        self.total = total
        self.limitation = limitation
        self.pk = pk

    def update_total(self, expense_repo: AbstractRepository[Expense]) -> None:
        """ Обновляет значение total за заданный период в атрибуте period """
        date = datetime.now()
        period_expenses = []
        if self.period == "day":
            date_str = date.isoformat()[:10]
            period_expenses = expense_repo.get_all(where={"expense_date": date_str})
        elif self.period.lower() == "week":
            for _ in range(7):
                date_str = date.isoformat()[:10]
                period_expenses += expense_repo.get_all(where={"expense_date": date_str})
                date = date - timedelta(days=1)
        elif self.period.lower() == "month":
            for _ in range(30):
                date_str = date.isoformat()[:10]
                period_expenses += expense_repo.get_all(where={"expense_date": date_str})
                date = date - timedelta(days=1)
        self.total = sum(exp.amount for exp in period_expenses)
