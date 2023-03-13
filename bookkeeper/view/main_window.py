"""
Основное окно приложения
"""
# pylint: disable=no-name-in-module
# pylint: disable=c-extension-no-member
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
import sys
from typing import Any
from PySide6 import QtWidgets
from bookkeeper.view.budget_view import BudgetTableGroup
from bookkeeper.view.expenses_view import ExpensesTableGroup
from bookkeeper.view.new_expense import NewExpenseGroup
from bookkeeper.view.edit_categories_button import EditCategoriesButton


class MainWindow(QtWidgets.QWidget):
    """ Класс, описывающий основное окно приложения"""
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Bookkeeper")
        self.vbox = QtWidgets.QVBoxLayout()
        # Список расходов
        self.expenses_table = ExpensesTableGroup()
        self.vbox.addWidget(self.expenses_table, stretch=10)
        # Бюджет
        self.budget_table = BudgetTableGroup()
        self.vbox.addWidget(self.budget_table, stretch=10)

        self.hbox = QtWidgets.QHBoxLayout()
        # Добавить трату
        self.new_expense = NewExpenseGroup()
        self.hbox.addWidget(self.new_expense, stretch=1)
        # Кнопка редактирования
        self.edit_category_button = EditCategoriesButton()
        self.hbox.addWidget(self.edit_category_button, stretch=1)

        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.resize(800, 800)
window.show()
sys.exit(app.exec())
