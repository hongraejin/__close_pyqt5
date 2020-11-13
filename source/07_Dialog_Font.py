import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication

class myExample(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton("Dialog",self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # btn.move(20,20)
        btn.clicked.connect(self.showDialog)

        self.label = QLabel("Know Better", self)
        # self.label.move(200,150)

        vbox.addWidget(btn)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setGeometry(300,300,500,400)
        self.setWindowTitle('Input Example')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        print(font)

        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myex = myExample()
    sys.exit(app.exec_())