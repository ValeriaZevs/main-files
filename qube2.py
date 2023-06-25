import sys
import math
from PyQt5 import uic
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
        uic.loadUi('image3.ui', self)
        self.setWindowTitle('Квадрат-объектив')
        self.t = False
        self.btn.clicked.connect(self.dopaint)
        self.line1.setText('0.9')
        self.line2.setText('5')

    def dopaint(self):
        self.t = True
        self.repaint()

    def paintEvent(self, event):
        if self.t:
            painter = QPainter()
            painter.begin(self)
            self.paintfigure(painter)
            painter.end()
            #self.update()

    def paintfigure(self, painter):
        k = float(self.line1.text())
        n = int(self.line2.text())
        delta = round(100 - k * 100)
        alpha = 0
        side = 300
        painter.setPen(QColor('red'))
        painter.translate(300, 300)
        for _ in range(n):
            painter.rotate(alpha)
            painter.drawRect(-side // 2, -side // 2, side, side)
            alpha += delta
            side *= k
            side = round(side)
        self.t = False
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())