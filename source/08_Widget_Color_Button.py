from PyQt5.QtWidgets import QWidget, QPushButton, QFrame,QApplication
from PyQt5.QtGui import QColor
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.col = QColor(0,0,0,0.5)

        redbutton = QPushButton('red',self)
        redbutton.setCheckable(True)
        redbutton.move(10,10)
        redbutton.clicked.connect(self.setColor)
        

        greenbutton = QPushButton('green',self)
        greenbutton.setCheckable(True)
        greenbutton.move(10,60)
        greenbutton.clicked.connect(self.setColor)
        

        bluebutton = QPushButton('blue',self)
        bluebutton.setCheckable(True)
        bluebutton.move(10,110)
        bluebutton.clicked.connect(self.setColor)

        self.frame = QFrame(self)
        self.frame.setGeometry(250 ,0,200,200)
        self.frame.setStyleSheet("QWidget {background-color : %s}" % self.col.name())


        self.setGeometry(300,300,500,400)
        self.show()


    # button 에 연결하는 callback 함수는 두가지 유형이 가능
    # setColor(self)
    # setColor(self, signal)
    # setChechable(True)를 선태갛지 않으면 계속 False 값이 들어간다.
    def setColor(self, pressed):
        sender = self.sender()
        print("버튼 눌림")
        print("thing", pressed)
        if pressed:
            val = 255
        else:
            val = 0

        if sender.text() =="red":self.col.setRed(val)
        elif sender.text() == 'green': self.col.setGreen(val)
        elif sender.text() == 'blue': self.col.setBlue(val)

        self.frame.setStyleSheet("QWidget {background-color : %s}" % self.col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())