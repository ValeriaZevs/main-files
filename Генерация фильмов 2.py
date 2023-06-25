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
        uic.loadUi('Фильмотека.ui', self)
        self.setWindowTitle('Фильмотека')
        self.btn.clicked.connect(self.run)
        self.second_form = Add()
        self.second_form.setUpdatesEnabled(True)
        if self.second_form.close():
            self.new()

    def run(self):
        self.second_form.show()

    def new(self):
        self.table.clear()
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        s = cur.execute(f"SELECT * from films").fetchall()
        r = 0
        self.table.setRowCount(len(s))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('ID', 'Название', 'Год', 'Жанр', 'Продолжительность'))
        for i in s:
            for j in range(5):
                cellinfo = QTableWidgetItem(str(i[j]))
                self.table.setItem(r, j, cellinfo)
            r += 1
        con.close()


class Add(QMainWindow):
    def __init__(self):
        super().__init__()  # создаем окно
        uic.loadUi('add.ui', self)
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        self.a = self.cur.execute(f"SELECT * from genres").fetchall()
        for i in self.a:
            self.box.addItem(i[-1])
        self.btn.clicked.connect(self.run)

    def run(self):
        if len([i for i in self.line2.text() if i in '1234567890']) != len(self.line2.text()) or\
                len([i for i in self.line3.text() if i in '1234567890']) != len(self.line3.text()):
            self.state.setText('Лишние символы')
        elif int(self.line2.text()) > 2023:
            self.state.setText('Неправильный год')
        elif int(self.line3.text()) <= 0:
            self.state.setText('Неправильная длина')
        elif len(self.line.text()) != 0 and len(self.line2.text()) != 0 and len(self.line3.text()) != 0:
            s = self.cur.execute(f"SELECT * from films").fetchall()
            m = 0
            for i in s:
                if i[0] > m:
                    m = i[0]
            g = [i[0] for i in self.a if i[-1] == self.box.currentText()][0]
            self.cur.execute(f"INSERT INTO films VALUES ({m + 1}, '{self.line.text()}', '{self.line2.text()}',"
                             f" '{g}', '{self.line3.text()}')")
            self.con.commit()
            self.close()
        else:
            self.state.setText('Неправильно заполнено')


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

