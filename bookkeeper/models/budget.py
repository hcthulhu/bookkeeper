"""
Модель бюджета
"""

from dataclasses import dataclass


@dataclass
class Budget:
    """
    Бюджет, хранит срок рассмотрения в атрибуте period ("day", "week", "month"),
    категория расходов в атрибуте category,
    лимит расходов на заданный срок в атрибуте limit,
    """
    period: str
    category: int
    limitation: int
    pk: int = 0
