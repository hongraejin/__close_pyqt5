from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        label = QLabel(self)

        pixmap = QPixmap('business.jpg')
        label.setPixmap(pixmap)
        hbox.addWidget(label)

        self.setLayout(hbox)
        self.setGeometry(300,300,500,400)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())