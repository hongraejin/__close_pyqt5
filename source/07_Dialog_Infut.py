import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication

class myExample(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("dialog", self)
        self.btn.move(50,50)
        self.btn.clicked.connect(self.showDialog)

        self.lineedit = QLineEdit(self)
        self.lineedit.move(150,50)

        self.setGeometry(300,300,500,400)
        self.setWindowTitle('Input Example')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self,'Dialog Title', 'Inner Label')

        if ok:
            print("text", text, 'ok', ok)
            print("type of text", type(text))
            self.lineedit.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myex = myExample()
    sys.exit(app.exec_())