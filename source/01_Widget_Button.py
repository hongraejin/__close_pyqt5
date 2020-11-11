import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    mywidget = MyWidget()
    sys.exit(app.exec_())