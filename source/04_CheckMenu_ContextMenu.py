import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
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
        menu_view = menu.addMenu('View')


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

        view_status = QAction("Status 표시줄", self, checkable=True)
        view_status.setChecked(True)
        view_status.triggered.connect(self.togleStatus)
        menu_view.addAction(view_status)

        menu_file.addAction(file_exit)

        self.resize(500,400)
        self.show()

    def togleStatus(self,Status):
        if Status:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent):
        # print(QContextMenuEvent.pos())
        # print(QContextMenuEvent.x())
        # print(QContextMenuEvent.y())
        # print(self.mapToGlobal(QContextMenuEvent.pos()))
        # mapToGlobal 은 local 한 app 좌표에서 전체 화면으로 환산해줌
        # 순간적으로 menu라는 qwidget 을 화면에 띄운다고 생각하면 됨
        menu = QMenu(self)
        quit = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        print("action", action)
        print('quit', quit)
        if action == quit:
            # menu 를 띄위ㅓ서 받은 action 의 값이 return 되고, action (quit) 을 선택하면 같아진다.
            qApp.quit()
            print('일치 ')


if __name__ == '__main__':
    app = QApplication([])
    mywindow = MyWindow()
    sys.exit(app.exec_())
