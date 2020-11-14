from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QWidget
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 자주 발생할 수 있는 실수 "self" , 화면에 없는경우
    #
    def initUI(self):
        self.label = QLabel("please select", self)

        combobox = QComboBox(self)
        combobox.addItem('python')
        combobox.addItem('C')
        combobox.addItem('C++')
        combobox.addItem('Java')
        combobox.move(50,50)
        self.label.move(50,150)

        combobox.activated[str].connect(self.onActivate)

        self.setGeometry(300,300,500,400)
        self.show()

    def onActivate(self,text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())