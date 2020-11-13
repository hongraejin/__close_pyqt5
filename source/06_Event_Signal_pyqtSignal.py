import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()

class MyQMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.com = Communicate()
        self.com.closeApp.connect(self.close)
        # self.com.closeApp.connect(self.myfunc)
        # no signal , state

        self.setGeometry(300,300,500,400)
        self.setWindowTitle("pyqtSignal")
        self.show()

    def mousePressEvent(self, QMouseEvent):
        self.com.closeApp.emit()

    def myfunc(self):
        print('sig ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow  = MyQMainWindow()
    sys.exit(app.exec_())