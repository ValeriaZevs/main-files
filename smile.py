import sys
import math
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('smile.ui', self)
        self.slider.setValue(50)
        self.setWindowTitle('Рост хорошего настроения')
        self.x, self.y = 100, 100

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.scale(self.slider.value() / 100, self.slider.value() / 100)
        self.paintfigure(painter)
        painter.end()
        self.update()

    def paintfigure(self, painter):
        painter.setPen(QColor('red'))
        painter.drawEllipse(self.x + self.slider.value(), self.y + self.slider.value(), 600, 600)
        painter.drawEllipse(self.x + self.slider.value() + 120, self.y + self.slider.value() + 120, 120, 120)
        painter.drawEllipse(self.x + self.slider.value() + 360, self.y + self.slider.value() + 120, 120, 120)
        s = QRectF(self.x + self.slider.value() + 150, self.y + self.slider.value() + 300, 300.0, 180.0)
        painter.drawArc(s, 220 * 16, 100 * 16)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())

