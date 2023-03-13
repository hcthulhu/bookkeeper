from PySide6 import QtWidgets

from bookkeeper.view.modified_widgets import LabeledComboBoxInput, LabeledLineInput


class NewExpenseGroup(QtWidgets.QGroupBox):
    categories = [f"Категория {i}" for i in range(5)]
    def __init__(self, *args, **kwargs):
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

    def submit(self):
        print(f"Новая трата в категории {self.category_input.text()} на сумму {self.amount_input.text()} добавлена")
        self.amount_input.clear()
        self.category_input.clear()