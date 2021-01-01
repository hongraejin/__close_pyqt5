from PyQt5.QtWidgets import QApplication, QWidget
import sys


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200,200,500,500)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    sys.exit(app.exec_())
