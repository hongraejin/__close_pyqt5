import sys
from PyQt5.QtWidgets import *

class MyBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        title = QLabel("title")
        author = QLabel("author")
        review = QLabel("review ")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        # reviewEdit / rowSpan / columnSpan
        # comp QTextEdit() vs QLineEdit()
        # grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(500,500,500,300)
        self.setWindowTitle('grid with spacing')
        self.show()

if __name__ == '__main__':
    app =QApplication([])
    mybox = MyBox()
    sys.exit(app.exec_())