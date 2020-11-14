from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.progressbar= QProgressBar(self)
        self.progressbar.setGeometry(50,50,400,50)

        self.button = QPushButton('start', self)
        self.button.move(20,150)
        self.button.clicked.connect(self.buttonClicked)

        self.timer = QBasicTimer()
        self.progress_value = 0

        self.setGeometry(300,300,500,400)
        self.show()

    def timerEvent(self, QTimerEvent):
        if self.progress_value >=100:
            self.timer.stop()
            self.button.setText('finished')
            return

        self.progress_value += 1
        self.progressbar.setValue(self.progress_value)

    def buttonClicked(self):

        sender = self.sender()
        if sender.text() == 'finished':
            self.progress_value = 0
            self.progressbar.setValue(self.progress_value)
            self.button.setText('start')
            self.timer.stop()
            return

        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('start')
        else:
            self.timer.start(100,self)
            self.button.setText("stop")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())