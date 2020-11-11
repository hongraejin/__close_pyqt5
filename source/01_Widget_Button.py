import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton("button", self)
        button.resize(button.sizeHint())
        button.setToolTip('button ToolTip <b>bald</b>')
        button.move(25,25)

        self.setGeometry(600,300,500,500)
        self.setWindowTitle('First App')
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    mywidget = MyWidget()
    sys.exit(app.exec_())