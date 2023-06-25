import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sqlite3


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('Алфавитный указатель.ui', self)
        self.setWindowTitle('Алфавитный указатель')
        self.sp = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                   self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10,
                   self.pushButton_11, self.pushButton_21, self.pushButton_31, self.pushButton_20, self.pushButton_12,
                   self.pushButton_22, self.pushButton_32, self.pushButton_30, self.pushButton_13, self.pushButton_23,
                   self.pushButton_33, self.pushButton_14, self.pushButton_24, self.pushButton_15, self.pushButton_25,
                   self.pushButton_16, self.pushButton_26, self.pushButton_17, self.pushButton_27,
                   self.pushButton_18, self.pushButton_28, self.pushButton_19, self.pushButton_29]
        for i in self.sp:
            i.clicked.connect(self.run)
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()

    def run(self):
        self.table.clear()
        sender = self.sender()
        s = self.cur.execute(f"SELECT * from films WHERE title LIKE '{sender.text()}%'").fetchall()
        a = self.cur.execute(f"SELECT * from genres").fetchall()
        self.table.setRowCount(len(s))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('ID', 'Название', 'Год', 'Жанр', 'Продолжительность'))
        if len(s) != 0:
            self.label.setText(f'Найдено {len(s)}')
            r = 0
            for i in s:
                for j in range(5):
                    if j == 3:
                        for k in a:
                            if i[j] == k[0]:
                                cellinfo = QTableWidgetItem(k[1])
                                self.table.setItem(r, j, cellinfo)
                    else:
                        cellinfo = QTableWidgetItem(str(i[j]))
                        self.table.setItem(r, j, cellinfo)
                r += 1
        else:
            self.label.setText('Ничего не найдено')



if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

