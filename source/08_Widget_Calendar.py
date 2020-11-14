from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.clicked[QDate].connect(self.showDate)

        vbox.addWidget(calendar)

        self.label = QLabel(self)
        # 기본으로 연결된 날짜 선택
        date = calendar.selectedDate()
        self.label.setText(date.toString())
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setGeometry(300,300,500,400)
        self.show()

    # showDate(self):
    # showDate(self, state) :
    # def showDate(self):
    #     print("showDate")

    def showDate(self, Qdate):
        print(Qdate)
        self.label.setText(Qdate.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())