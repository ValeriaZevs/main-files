import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap, QBitmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('disappear.ui', self)
        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        self.orig_image = Image.open(self.filename)
        self.curr_image = Image.open(self.filename)
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.label.setPixmap(self.pixmap)
        self.slider.setValue(100)
        self.slider.valueChanged[int].connect(self.changeValue)
        self.setWindowTitle('Управление прозрачностью')

    def changeValue(self, value):
        self.curr_image = self.orig_image.copy()
        img = self.curr_image.convert('RGBA')
        x, y = img.size
        for i in range(x):
            for k in range(y):
                color = img.getpixel((i, k))
                color = color[:-1] + (value * 2,)
                img.putpixel((i, k), color)
        self.curr_image = img
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.label.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())

