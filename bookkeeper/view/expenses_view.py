from PySide6 import QtWidgets


class ExpensesTableWidget(QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
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

    def add_data(self, data: list[list[str]]):
        for i, row in enumerate(data):
            for j, x in enumerate(row):
                self.setItem(
                    i, j,
                    QtWidgets.QTableWidgetItem(x.capitalize())
                )

class ExpensesTableGroup(QtWidgets.QGroupBox):
    data = [["2023-10-01", str(10), "мясо", "комментарий"],
            ["2023-10-02", str(200), "продукты", ""],
            ["2023-10-03", str(3000), "сладости", ""],]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("<b>Последние траты</b>")
        self.vbox.addWidget(self.label)
        self.table = ExpensesTableWidget()
        self.table.add_data(self.data)
        self.vbox.addWidget(self.table)
        self.setLayout(self.vbox)