"""
Виджет для добавления новых расходов
"""
# mypy: disable-error-code="attr-defined,assignment"
# pylint: disable=no-name-in-module
# pylint: disable=c-extension-no-member
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
from typing import Any
from PySide6 import QtWidgets
from bookkeeper.view.modified_widgets import LabeledComboBoxInput, LabeledLineInput


class NewExpenseGroup(QtWidgets.QGroupBox):
    """ Класс, описывающий виджет для добавления новых расходов """
    categories = [f"Категория {i}" for i in range(5)]

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("<b>Новая трата</b>")
        self.vbox.addWidget(self.label)
        self.amount_input = LabeledLineInput("Сумма", "0")
        self.vbox.addWidget(self.amount_input)
        self.category_input = LabeledComboBoxInput("Категория", self.categories)
        self.vbox.addWidget(self.category_input)
        self.submit_button = QtWidgets.QPushButton('Добавить')
        self.submit_button.clicked.connect(self.submit)
        self.vbox.addWidget(self.submit_button)
        self.setLayout(self.vbox)

    def submit(self) -> None:
        """ Действие, вызываемое после нажатия кнопки """
        print(f"Добавлена новая трата в категории {self.category_input.text()} "
              f"на сумму {self.amount_input.text()}")
        self.category_input.clear()
        self.amount_input.clear()
