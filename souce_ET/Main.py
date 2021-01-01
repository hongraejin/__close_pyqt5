from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QGridLayout, QPushButton, QDialog
import sys
import os

class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.workdir = ""
        self.initUI()

    def initUI(self):

        self.layout = QGridLayout()

        self.btn_folder = QPushButton('폴더선택', self)
        self.btn_folder.clicked.connect(self.btn_folder_Clicked)
        self.layout.addWidget(self.btn_folder,0,0)

        self.btn_format = QPushButton("데이터 양식", self)
        self.btn_format.clicked.connect(self.btn_format_Clicked)
        self.layout.addWidget(self.btn_format,1,0)


        # self.btn_folder = QPushButton('폴더선택', self)
        # self.layout.addWidget(self.btn_folder,0,1)

        self.setLayout(self.layout)
        self.setGeometry(300,300,500,400)
        self.show()

    def btn_folder_Clicked(self):
        res = QFileDialog.getExistingDirectory()
        if res:
            self.workdir = res
            print("작업폴더설정 : ", self.workdir)

    def btn_format_Clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    app.exec_()