from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor
import sys

class MyColorDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0,0,0)

        self.btn = QPushButton('ColorDialog', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showColorDialog)

        self.frame = QFrame(self)
        self.frame.move(150,20)
        self.frame.setStyleSheet('QWidget {background-color:  %s}' % col.name())

        self.setGeometry(300,300,500,400)
        self.setWindowTitle('Color Example')
        self.show()

    def showColorDialog(self):
        color = QColorDialog.getColor()

        print(color)
        print("type",type(color))
        self.frame.setStyleSheet('QWidget {background-color: %s}' % color.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mycolordialog = MyColorDialog()
    sys.exit(app.exec_())
