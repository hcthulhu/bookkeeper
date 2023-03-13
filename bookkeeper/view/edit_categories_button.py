"""
Виджет кнопки для редактирования категорий
"""
# mypy: disable-error-code="attr-defined,assignment"
# pylint: disable=no-name-in-module
# pylint: disable=c-extension-no-member
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
from typing import Any
from PySide6 import QtWidgets


class EditCategoriesButton(QtWidgets.QGroupBox):
    """ Класс, описывающий виджет кнопки для редактирования категорий """
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("<b>Категории</b>")
        self.vbox.addWidget(self.label)
        self.edit_button = QtWidgets.QPushButton('Добавить')
        self.edit_button.clicked.connect(self.edit)
        self.vbox.addWidget(self.edit_button)
        self.setLayout(self.vbox)

    def edit(self) -> None:
        """ Действие, вызываемое после нажатия кнопки """
        print('Редактирование')
