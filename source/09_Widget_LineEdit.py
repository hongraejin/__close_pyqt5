from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.label = QLabel(self)
        lineedit = QLineEdit(self)
        
        lineedit.move(50,50)
        lineedit.textChanged[str].connect(self.showChange)
        
        
        self.setGeometry(300,300,500,400)
        self.show()
    
    # def showChange(self):
    #     print("진입")
    def showChange (self,text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())