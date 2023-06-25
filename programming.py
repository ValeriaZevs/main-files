import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Управление НЛО')
        self.t = 0
        self.x, self.y = 100, 100
        self.label = QLabel(self)
        self.label.setGeometry(self.x, self.y, 100, 100)
        self.pix = QPixmap('cat1.png')
        self.label.setPixmap(self.pix)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.t = 1
            self.paintfigure()
        if event.key() == Qt.Key_Right:
            self.t = 2
            self.paintfigure()
        if event.key() == Qt.Key_Down:
            self.t = 3
            self.paintfigure()
        if event.key() == Qt.Key_Left:
            self.t = 4
            self.paintfigure()
        #self.update()

    def paintfigure(self):
        if self.t == 1:
            self.y -= 10
            if self.y + 30 <= 0:
                self.y = 330
        if self.t == 2:
            self.x += 10
            if self.x + 10 >= 360:
                self.x = 0
        if self.t == 3:
            self.y += 10
            if self.y + 10 >= 350:
                self.y = -20
        if self.t == 4:
            self.x -= 10
            if self.x + 10 <= 0:
                self.x = 360
        self.label.move(self.x, self.y)
        self.update()
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())