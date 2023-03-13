"""
Модель бюджета
"""
from bookkeeper.repository.abstract_repository import AbstractRepository
from bookkeeper.models.expense import Expense
from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class Budget:
    """
    Бюджет, хранит срок рассмотрения в атрибуте period ("day", "week", "month"),
    потраченная сумма за рассматриваемый срок в атрибуте sum,
    лимит расходов на заданный срок в атрибуте limitation,
    """
    period: str
    sum: int
    limitation: int
    pk: int = 0

    def __init__(self, period: str, sum: int, limitation: int, pk: int = 0):
        if period not in ["day", "week", "month"]:
            raise ValueError(f'unknown period "{period}" '
                             + f'should be "day", "week" or "month"')
        self.period = period
        self.sum = sum
        self.limitation = limitation
        self.pk = pk

    def update_sum(self, expense_repo: AbstractRepository[Expense]) -> None:
        date = datetime.now()
        if self.period == "day":
            date_str = date.isoformat()[:10]  # YYYY-MM-DD format
            period_expenses = expense_repo.get_all(where={"expense_date": date_str})
        elif self.period.lower() == "week":
            period_expenses = []
            for i in range(7):
                date_str = date.isoformat()[:10]
                period_expenses += expense_repo.get_all(where={"expense_date": date_str})
                date = date - timedelta(days=1)
        elif self.period.lower() == "month":
            period_expenses = []
            for i in range(30):
                date_str = date.isoformat()[:10]
                period_expenses += expense_repo.get_all(where={"expense_date": date_str})
                date = date - timedelta(days=1)
        self.sum = sum([exp.amount for exp in period_expenses])