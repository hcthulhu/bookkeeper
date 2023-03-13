"""
Виджет с таблицей расходов
"""
# mypy: disable-error-code="attr-defined"
# pylint: disable=no-name-in-module
# pylint: disable=c-extension-no-member
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
from typing import Any
from PySide6 import QtWidgets


class ExpensesTableWidget(QtWidgets.QTableWidget):
    """ Класс, описывающий виджет с таблицей расходов """
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.setColumnCount(4)
        self.setRowCount(30)
        headers = "Дата Сумма Категория Комментарий".split()
        self.setHorizontalHeaderLabels(headers)
        header = self.horizontalHeader()
        header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(
            3, QtWidgets.QHeaderView.Stretch)
        self.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()

    def add_data(self, data: list[list[str]]) -> None:
        """ Внесение данных в таблицу """
        for table_row, row in enumerate(data):
            for table_col, text in enumerate(row):
                self.setItem(
                    table_row, table_col,
                    QtWidgets.QTableWidgetItem(text.capitalize())
                )


class ExpensesTableGroup(QtWidgets.QGroupBox):
    """ Группа с таблицей расходов """
    data = [["2023-10-01", str(10), "мясо", "комментарий"],
            ["2023-10-02", str(200), "продукты", ""],
            ["2023-10-03", str(3000), "сладости", ""],]

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("<b>Последние траты</b>")
        self.vbox.addWidget(self.label)
        self.table = ExpensesTableWidget()
        self.table.add_data(self.data)
        self.vbox.addWidget(self.table)
        self.setLayout(self.vbox)
