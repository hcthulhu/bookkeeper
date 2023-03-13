"""
Модифицированные дополнительные виджеты
"""
# mypy: disable-error-code="attr-defined,assignment"
# pylint: disable=no-name-in-module
# pylint: disable=c-extension-no-member
# pylint: disable=too-many-instance-attributes
from typing import Any
from PySide6 import QtWidgets


class LabeledLineInput(QtWidgets.QWidget):
    """ Строка для ввода с подписью """
    def __init__(self, text: str, placeholder: str, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.placeholder = placeholder
        self.layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(text)
        self.layout.addWidget(self.label, stretch=1)
        self.input = QtWidgets.QLineEdit(self.placeholder)
        self.layout.addWidget(self.input, stretch=5)
        self.setLayout(self.layout)  # type: ignore

    def clear(self) -> None:
        """ Вернуть начальное значение ввода """
        self.input.setText(self.placeholder)

    def text(self) -> str:
        """ Получить введенный текст """
        return self.input.text()


class LabeledComboBoxInput(QtWidgets.QWidget):
    """ Выпадающий список для ввода с подписью """
    def __init__(self, text: str, items: list[str], *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(text)
        self.layout.addWidget(self.label, stretch=1)
        self.combo_box = QtWidgets.QComboBox()
        self.items = items
        self.combo_box.addItems(items)
        self.combo_box.setPlaceholderText(items[0])
        self.combo_box.setLineEdit(QtWidgets.QLineEdit())
        self.layout.addWidget(self.combo_box, stretch=5)
        self.setLayout(self.layout)  # type: ignore

    def clear(self) -> None:
        """ Вернуть начальное значение ввода """
        self.combo_box.setCurrentText(self.combo_box.placeholderText())

    def text(self) -> str:
        """ Получить введенный текст """
        return self.combo_box.currentText()
