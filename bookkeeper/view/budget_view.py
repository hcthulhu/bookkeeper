from PySide6 import QtWidgets


class BudgetTableWidget(QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setColumnCount(2)
        self.setRowCount(3)
        hheaders = "Сумма Бюджет".split()
        self.setHorizontalHeaderLabels(hheaders)
        vheaders = "День Неделя Месяц".split()
        self.setVerticalHeaderLabels(vheaders)
        for h in [self.horizontalHeader(), self.verticalHeader(),]:
            h.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

    def add_data(self, data: list[list[str]]):
        for i, row in enumerate(data):
            for j, x in enumerate(row):
                self.setItem(
                    i, j,
                    QtWidgets.QTableWidgetItem(x.capitalize())
                )

class BudgetTableGroup(QtWidgets.QGroupBox):
    data = [['500', '1000'],
            ['2000', '7000'],
            ['5000', '30000'],]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("<b>Бюджет</b>")
        self.vbox.addWidget(self.label)
        self.table = BudgetTableWidget()
        self.table.add_data(self.data)
        self.vbox.addWidget(self.table)
        self.setLayout(self.vbox)