import sys
import random
from math import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


SCREEN_SIZE = [500, 500]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('6angle.ui', self)
        self.setWindowTitle('Не квадрат-объектив')
        self.t = False
        self.btn.clicked.connect(self.dopaint)
        self.line1.setText('0.9')
        self.line2.setText('10')
        self.line3.setText('6')
        self.btn.clicked.connect(self.run)
        self.color = ''

    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color.name()
            self.dopaint()

    def dopaint(self):
        self.t = True
        self.repaint()

    def paintEvent(self, event):
        if self.t:
            painter = QPainter()
            painter.begin(self)
            self.paintfigure(painter)
            painter.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def paintfigure(self, qp):
        pen = QPen(QColor(self.color), 2)
        qp.setPen(pen)
        k = float(self.line1.text())
        n = int(self.line2.text())
        m = int(self.line3.text())
        side = 200
        qp.translate(0, 0)
        for a in range(n):
            nodes = [(side * cos(i * 2 * pi / m),
                      side * sin(i * 2 * pi / m))
                     for i in range(m)]
            nodes2 = [(int(self.xs(node[0])),
                       int(self.ys(node[1]))) for node in nodes]
            for i in range(-1, len(nodes2) - 1):
                qp.drawLine(*nodes2[i], *nodes2[i + 1])
            qp.rotate(k)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

