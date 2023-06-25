import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('bible.ui', self)
        self.setWindowTitle('Каталог библиотеки')
        self.btn.clicked.connect(self.run)
        self.box.addItems(["Автор", "Название"])
        self.conn = sqlite3.connect('books.sqlite')
        self.cur = self.conn.cursor()

    def run(self):
        t = self.line.text()
        n = self.box.currentText()
        info = []
        if n == 'Автор':
            info = self.cur.execute(f"select * from Книги where Автор LIKE '%{t}%'").fetchall()
        elif n == 'Название':
            info = self.cur.execute(f"select * from Книги where Название LIKE '%{t}%'").fetchall()
        print(info)
        for i in info:
            btn = QPushButton(i[1])
            btn.clicked.connect(self.run2)
            item = QListWidgetItem(self.list)
            self.list.setItemWidget(item, btn)

    def run2(self):
        n = self.sender()
        self.second_form = Add(n.text())
        self.second_form.setUpdatesEnabled(True)
        self.second_form.show()


class Add(QMainWindow):
    def __init__(self, n):
        super().__init__()
        uic.loadUi('bookpic.ui', self)
        self.conn = sqlite3.connect('books.sqlite')
        self.cur = self.conn.cursor()
        a = self.cur.execute(f"select * from Книги where Название = '{n}'").fetchall()[0]
        self.name.setText(a[1])
        self.author.setText(a[2])
        self.year.setText(a[3])
        self.genre.setText(a[4])
        self.pix = QPixmap(a[-1])
        self.pic.setPixmap(self.pix)




if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

