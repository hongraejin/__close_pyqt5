import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class AbsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        lbl1 = QLabel("Zetcode", self)
        lbl1.move(15,10)

        lbl2 = QLabel("tutorials", self)
        lbl2.move(35,40)

        lbl3 = QLabel("fro programmers", self)
        lbl3.move(55,70)

        self.show()



if __name__ == '__main__':
    app = QApplication([])
    abdwidget = AbsWidget()
    sys.exit(app.exec_())