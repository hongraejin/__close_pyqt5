from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys

class MyButton(QPushButton):
    def __init__(self,title,parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, QMouseEvent):
        # 마우스 움직임에 대한 대응
        # 오른쪽 마우스만 받아들임
        if QMouseEvent.buttons() != Qt.RightButton:
            return

        # 멀티미디어 데이터 다룸룸
        mimeDate = QMimeData()

        # Button 자체에는 Drag 에 대한 데이터가 없어서 내가 추가해주어야 한다.
        drag = QDrag(self)
        drag.setMimeData(mimeDate)
        # 활성화
        drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, QMouseEvent):
        super().mousePressEvent(QMouseEvent)

        if QMouseEvent.button() == Qt.LeftButton:
            print("pressed")

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.mybutton = MyButton("mybutton", self)
        self.mybutton.move(100,65)

        self.setGeometry(300,300,500,400)
        self.show()

    def dragEnterEvent(self, QDragEnterEvent):
        QDragEnterEvent.accept()
        

    def dropEvent(self, QDropEvent):
        # 드래그 하다가 마우스를 놓았을 때
        position = QDropEvent.pos()
        buttonsize = self.mybutton.size()

        # position_x , position_y = position.x(), position.y()
        # print(position_x, position_y)
        # buttonsize_x, buttonsize_y =  buttonsize.width(), buttonsize.height()
        # button_half_x , button_half_y = buttonsize_x //2, buttonsize_y//2
        # print(button_half_x, button_half_y)
        # to_x , to_y = position_x+button_half_x, position_y+button_half_y
        # self.mybutton.move(to_x , to_y)
        self.mybutton.move(position)
        # 동작을 다하고 반영한다
        QDropEvent.accept()
        

if __name__ == '__main__':
    # 다양한 어플리케이션 실행방식
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())