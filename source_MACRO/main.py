from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QGroupBox, QVBoxLayout, QSizePolicy,QProgressBar, QLabel, QMessageBox
import sys
import glob
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp, QFileDialog
from PyQt5.QtCore import QCoreApplication, QBasicTimer

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.createProgressBars()
        self.timer = QBasicTimer()
        self.classfyFolder = "."
        self.metFolder = "."

        grid = QGridLayout()
        grid.addWidget(self.createClassfyMImage(),0,0)
        grid.addWidget(self.createMetMImage(), 0, 1)

        self.setLayout(grid)
        self.setGeometry(200,200,500,250)
        self.show()

    def createProgressBars(self):
        self.progressbarClassfy= QProgressBar(self)
        self.progressbarClassfy.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.progressbarClassfy.setMinimumHeight(50)
        self.progressbarClassfy.setMinimumWidth(50)
        self.progressbarClassfy_value = 0


        self.progressbarMet= QProgressBar(self)
        self.progressbarMet.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.progressbarMet.setMinimumHeight(50)
        self.progressbarMet.setMinimumWidth(50)
        self.progressbarMet_value = 0

        self.progressBars = [self.progressbarClassfy, self.progressbarMet]


    # 매크로 이미지 분류기
    def createClassfyMImage(self):
        groupbox = QGroupBox('1. MACRO 이미지 분류')

        folderSettingButton = QPushButton("분류폴더 설정")
        folderSettingButton.resize(100,50)
        folderSettingButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        folderSettingButton.setMinimumHeight(50)
        folderSettingButton.setMinimumWidth(50)
        folderSettingButton.clicked.connect(self.ClassfyFolderSettingButtonClicked)

        startClassfyButton = QPushButton("이미지분류 시작")
        startClassfyButton.resize(100,50)

        startClassfyButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        startClassfyButton.setMinimumHeight(50)
        startClassfyButton.setMinimumWidth(50)
        startClassfyButton.clicked.connect(self.buttonClicked)

        self.statusClassfyLabel = QLabel("")

        vbox = QVBoxLayout()
        vbox.addWidget(folderSettingButton)
        vbox.addWidget(startClassfyButton)
        vbox.addStretch(1)
        vbox.addWidget(self.statusClassfyLabel)
        vbox.addWidget(self.progressbarClassfy)
        vbox.addStretch(1)

        groupbox.setLayout(vbox)

        return groupbox

    # 매크로 이미지 처리기
    def createMetMImage(self):
        groupbox = QGroupBox('2. 지름 측정')

        folderSettingButton = QPushButton("매크로폴더 설정")
        folderSettingButton.resize(100,50)
        folderSettingButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        folderSettingButton.setMinimumHeight(50)
        folderSettingButton.setMinimumWidth(50)
        folderSettingButton.clicked.connect(self.MetFolderSettingButtonClicked)

        startClassfyButton = QPushButton("지름측정 시작")
        startClassfyButton.resize(100,50)
        startClassfyButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        startClassfyButton.setMinimumHeight(50)
        startClassfyButton.setMinimumWidth(50)
        startClassfyButton.clicked.connect(self.buttonClicked)

        self.statusMetLabel = QLabel()


        vbox = QVBoxLayout()
        vbox.addWidget(folderSettingButton)
        vbox.addWidget(startClassfyButton)
        vbox.addStretch(1)
        vbox.addWidget(self.statusMetLabel)
        vbox.addWidget(self.progressbarMet)
        vbox.addStretch(1)

        groupbox.setLayout(vbox)

        return groupbox

    def ClassfyFolderSettingButtonClicked(self):

        path = QFileDialog.getExistingDirectory(self)
        if path:
            self.classfyFolder = path
            statusString = "선택한 폴더 :  \n" + self.classfyFolder
            self.statusClassfyLabel.setText(statusString)
            self.progressbarClassfy_value = 0
            self.progressbarClassfy.setValue(self.progressbarClassfy_value)
        else:
            statusString = "폴더 설정을 취소하였습니다"
            self.statusClassfyLabel.setText(statusString)

    def MetFolderSettingButtonClicked(self):

        path = QFileDialog.getExistingDirectory(self)
        if path:
            self.metFolder = path
            statusString = "선택한 폴더 :  \n"+ self.metFolder
            self.statusMetLabel.setText(statusString)
            self.progressbarMet_value = 0
            self.progressbarMet.setValue(self.progressbarMet_value)
        else:
            statusString = "폴더 설정을 취소하였습니다"
            self.statusMetLabel.setText(statusString)


    def buttonClicked(self):

        sender = self.sender()
        # 이미지분류 버튼
        if sender.text() == "이미지분류 시작":

            if (not self.classfyFolder) or (self.classfyFolder == "."):
                QMessageBox.information(self, "폴더 설정", "폴더 설정이 필요합니다")

            else:
                if self.timer.isActive():
                    print('진행중')
                else:
                    self.timer.start(100,self)
                    print("스타트")

        # 지름측정 버튼
        elif sender.text() == "지름측정 시작":
            if (not self.metFolder) or (self.metFolder == "."):
                QMessageBox.information(self, "폴더 설정", "폴더 설정이 필요합니다")

            self.progressbarMet_value = 0
            self.progressbarMet.setValue(self.progressbarMet_value)
            return



    def timerEvent(self, QTimerEvent):
        if self.progressbarClassfy_value >=100:
            self.timer.stop()
            return

        self.progressbarClassfy_value += 1
        self.progressbarClassfy.setValue(self.progressbarClassfy_value)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("문의사항 : hongrae.jin@samsung.com")

        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        menu_edit = menu.addMenu("Edit")
        menu_view = menu.addMenu('View')


        file_exit = QAction("Exit", self)
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("Quit")
        file_exit.triggered.connect(QCoreApplication.instance().exit)

        # # 세부사항을 모아서 올라감
        # file_new = QMenu("New", self)
        # new_txt = QAction("Text 파일", self)
        # new_py = QAction("Python 파일", self)
        # file_new.addAction(new_txt)
        # file_new.addAction(new_py)
        # menu_file.addMenu(file_new)

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
            qApp.quit()
            print('일치 ')


if __name__ == '__main__':
    app = QApplication([])
    mywindow = MyWindow()
    sys.exit(app.exec_())
