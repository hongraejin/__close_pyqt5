import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton("button", self)
        button.resize(button.sizeHint())
        button.setToolTip('button ToolTip <b>bald</b>')
        button.move(25,25)
        button.clicked.connect(QCoreApplication.instance().exit)

        self.setGeometry(600,300,500,500)
        self.setWindowTitle('First App')
        self.show()

    def closeEvent(self, QCloseEvent):
        response = QMessageBox.question(self,'quit check','Do you really want to exit?',
                             QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            print("진입")
            QCloseEvent.accept()
        elif response == QMessageBox.No:
            QCloseEvent.ignore()




if __name__ == '__main__':
    app = QApplication([])
    mywidget = MyWidget()
    sys.exit(app.exec_())