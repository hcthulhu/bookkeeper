import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QAction

from bookkeeper.view.budget_view import BudgetTableGroup
from bookkeeper.view.new_expense import NewExpenseGroup
from bookkeeper.view.expenses_view import ExpensesTableGroup


class MainWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vbox = QtWidgets.QVBoxLayout()
        # Список расходов
        self.expenses_table = ExpensesTableGroup()
        self.vbox.addWidget(self.expenses_table, stretch=10)
        self.setLayout(self.vbox)
        # Бюджет
        self.budget_table = BudgetTableGroup()
        self.vbox.addWidget(self.budget_table, stretch=6)
        # Добавить трату
        self.new_expense = NewExpenseGroup()
        self.vbox.addWidget(self.new_expense, stretch=1)
        # Кнопка редактирования
        self.edit_button = QtWidgets.QPushButton('Редактировать')
        self.edit_button.clicked.connect(self.editing())
        self.vbox.addWidget(self.edit_button, stretch=1)

    def editing(self):
        print("Редактирование")



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bookkeeper")
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

        toolbar = QtWidgets.QToolBar("My main toolbar")
        button_action = QAction("toolBar", self)
        button_action.triggered.connect(lambda s: print(s))
        toolbar.addAction(button_action)
        self.addToolBar(toolbar)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.resize(800, 800)
window.show()
sys.exit(app.exec())