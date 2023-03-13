"""
Виджет с таблица бюджета
"""
# mypy: disable-error-code="attr-defined"
# pylint: disable=no-name-in-module
# pylint: disable=c-extension-no-member
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
from typing import Any
from PySide6 import QtWidgets


class BudgetTableWidget(QtWidgets.QTableWidget):
    """ Класс, описывающий виджет с таблица бюджета """
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.setColumnCount(2)
        self.setRowCount(3)
        hheaders = "Сумма Бюджет".split()
        self.setHorizontalHeaderLabels(hheaders)
        vheaders = "День Неделя Месяц".split()
        self.setVerticalHeaderLabels(vheaders)
        for header in [self.horizontalHeader(), self.verticalHeader(),]:
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

    def add_data(self, data: list[list[str]]) -> None:
        """ Внесение данных в таблицу """
        for table_row, row in enumerate(data):
            for table_col, text in enumerate(row):
                self.setItem(
                    table_row, table_col,
                    QtWidgets.QTableWidgetItem(text.capitalize())
                )


class BudgetTableGroup(QtWidgets.QGroupBox):
    """ Группа с таблицей бюджета """
    data = [['500', '1000'],
            ['2000', '7000'],
            ['5000', '30000'],]

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("<b>Бюджет</b>")
        self.vbox.addWidget(self.label)
        self.table = BudgetTableWidget()
        self.table.add_data(self.data)
        self.vbox.addWidget(self.table)
        self.setLayout(self.vbox)
