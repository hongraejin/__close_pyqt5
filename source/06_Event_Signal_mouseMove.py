import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class MyKeyPressWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x : {0}, y : {1}".format(x,y)
        self.label = QLabel(self.text, self)

        grid.addWidget(self.label,0,0, Qt.AlignTop)
        self.setMouseTracking(True)
        # if not ?

        # print(Qt.AlignTop)
        self.setLayout(grid)

        self.show()
        self.setGeometry(300,300,500,400)
        self.setWindowTitle("Key Press Widget")

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()

        text = "x : {} , y : {}".format(x, y)
        self.label.setText(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mykeypresswidget = MyKeyPressWidget()
    sys.exit(app.exec_())