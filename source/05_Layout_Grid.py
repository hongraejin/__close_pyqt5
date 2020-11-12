import sys
from PyQt5.QtWidgets import *

class MyBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['cls','bck','','close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+'
                 ]
        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)

        self.setGeometry(500,500,500,300)
        self.setWindowTitle('box and stretch')

        self.show()

if __name__ == '__main__':
    app =QApplication([])
    mybox = MyBox()
    sys.exit(app.exec_())