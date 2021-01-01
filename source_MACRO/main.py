from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QGroupBox, QVBoxLayout, QSizePolicy,QProgressBar

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication, QBasicTimer

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.progressbar= QProgressBar(self)
        self.progressbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.progressbar.setMinimumHeight(50)
        self.progressbar.setMinimumWidth(50)
        self.timer = QBasicTimer()
        self.progress_value = 0

        grid = QGridLayout()
        grid.addWidget(self.createClassfyMImage(),0,0)
        grid.addWidget(self.createMetMImage(), 0, 1)


        #
        # self.classfyQPushButton = QPushButton('MACRO 이미지 분류기', self)
        # self.classfyQPushButton.move(50,50)


        self.setLayout(grid)

        self.setGeometry(200,200,500,250)
        self.show()

    # 매크로 이미지 분류기
    def createClassfyMImage(self):
        groupbox = QGroupBox('1. MACRO 이미지 분류')

        folderSettingButton = QPushButton("폴더 설정")
        folderSettingButton.resize(100,50)
        folderSettingButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        folderSettingButton.setMinimumHeight(50)
        folderSettingButton.setMinimumWidth(50)

        startClassfyButton = QPushButton("시작")
        startClassfyButton.resize(100,50)
        startClassfyButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        startClassfyButton.setMinimumHeight(50)
        startClassfyButton.setMinimumWidth(50)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addWidget(folderSettingButton)
        vbox.addWidget(startClassfyButton)
        vbox.addStretch(1)
        vbox.addWidget(self.progressbar)
        vbox.addStretch(1)


        groupbox.setLayout(vbox)

        return groupbox

    # 매크로 이미지 처리기
    def createMetMImage(self):
        groupbox = QGroupBox('2. 지름 측정')

        folderSettingButton = QPushButton("폴더 설정")
        folderSettingButton.resize(100,50)
        folderSettingButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        folderSettingButton.setMinimumHeight(50)
        folderSettingButton.setMinimumWidth(50)

        startClassfyButton = QPushButton("시작")
        startClassfyButton.resize(100,50)
        startClassfyButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        startClassfyButton.setMinimumHeight(50)
        startClassfyButton.setMinimumWidth(50)

        vbox = QVBoxLayout()
        # vbox.addStretch(1)
        vbox.addWidget(folderSettingButton)
        vbox.addWidget(startClassfyButton)
        vbox.addStretch(1)

        groupbox.setLayout(vbox)

        return groupbox

    def timerEvent(self, QTimerEvent):
        if self.progress_value >=100:
            self.timer.stop()
            self.button.setText('finished')
            return

        self.progress_value += 1
        self.progressbar.setValue(self.progress_value)

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

        self.setCentralWidget(MyWidget())

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
