import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class MyQMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # btn1 = QPushButton("button1)"
        btn1 = QPushButton("button1", self)
        btn1.move(30,50)
        btn2 = QPushButton("button2", self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        # init statusBar
        self.statusBar()

        self.setGeometry(300,300,500,400)
        self.setWindowTitle("sender")
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " has been pressed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow  = MyQMainWindow()
    sys.exit(app.exec_())