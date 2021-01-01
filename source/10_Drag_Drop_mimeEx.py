from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
import sys

class MyButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, QDragEnterEvent):
        if QDragEnterEvent.mimeData().hasFormat('text/plain'):
            QDragEnterEvent.accept()
        else:
            QDragEnterEvent.ignore()

    def dropEvent(self, QDropEvent):
        self.setText(QDropEvent.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lineedit = QLineEdit("",self)
        lineedit.setDragEnabled(True)
        lineedit.move(30,65)

        button = MyButton('mybutton', self)
        button.move(190, 65)

        self.setGeometry(300,300,500,400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()