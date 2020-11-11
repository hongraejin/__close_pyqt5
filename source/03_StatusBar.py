import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.statusBar()
        # self.statusBar().showMessage("Hello StatusBar")
        statusBar = self.statusBar()
        statusBar.showMessage("Hello StatusBar")

        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        menu_edit = menu.addMenu("Edit")

        file_exit = QAction("Exit", self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("Quit")

        menu_file.addAction(file_exit)

        self.resize(500,400)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    mywindow = MyWindow()
    sys.exit(app.exec_())
