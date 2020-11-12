import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication
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
        file_exit.triggered.connect(QCoreApplication.instance().exit)

        # 세부사항을 모아서 올라감
        file_new = QMenu("New", self)
        new_txt = QAction("Text 파일", self)
        new_py = QAction("Python 파일", self)
        file_new.addAction(new_txt)
        file_new.addAction(new_py)
        menu_file.addMenu(file_new)


        menu_file.addAction(file_exit)

        self.resize(500,400)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    mywindow = MyWindow()
    sys.exit(app.exec_())
