import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class MyKeyPressWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.show()
        self.setGeometry(300,300,500,400)
        self.setWindowTitle("Key Press Widget")

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            # print(Qt.Key_Escape)
            self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mykeypresswidget = MyKeyPressWidget()
    sys.exit(app.exec_())