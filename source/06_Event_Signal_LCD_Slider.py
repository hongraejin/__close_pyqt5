import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication)

class MyLCDWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        lcdnumber = QLCDNumber()
        slider = QSlider(Qt.Horizontal , self)
        # slider = QSlider()

        vbox.addWidget(lcdnumber)
        vbox.addWidget(slider)

        slider.valueChanged.connect(lcdnumber.display)
        # slider value connect
        # display(self, str)

        self.setLayout(vbox)

        self.show()
        self.setGeometry(300,300,500,400)
        self.setWindowTitle("LAD connect")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mylcdwidget = MyLCDWidget()
    sys.exit(app.exec_())