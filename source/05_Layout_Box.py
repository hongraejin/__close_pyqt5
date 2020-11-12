import sys
from PyQt5.QtWidgets import *

class MyBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancleButton = QPushButton("Cancle")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancleButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(500,500,500,300)
        self.setWindowTitle('box and stretch')

        self.show()

if __name__ == '__main__':
    app =QApplication([])
    mybox = MyBox()
    sys.exit(app.exec_())