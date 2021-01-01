from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
import sys, random

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sentence = 'this is example'


        self.setGeometry(300,300,500,400)
        self.show()

    # 창이 활성화되거나 비활성화될 때 실행됨
    def paintEvent(self, QPaintEvent):
        # painter 관련된 작업은 begin과 end 사이에 위치해야함
        # print('1')
        painter = QPainter()
        # print('2')
        painter.begin(self)
        # print('3')
        self.drawText(QPaintEvent, painter)
        # print('4')
        painter.end()
        # print('5')


    def drawText(self,event, painter):
        # print('a')
        painter.setPen(QColor(155,30,3))
        # print('b')
        painter.setFont(QFont('gulim',10))
        # print('c')
        painter.drawText(event.rect(), Qt.AlignHCenter, self.sentence)
        # print('d')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()