import sys
from PyQt5.QtWidgets import *
import random_lunch
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtGui


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = '점심조 정하기!'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.textbox = QLabel(self)
        self.textbox.move(20, 20)
        self.textbox.resize(600, 350)
        self.textbox.setFont(QtGui.QFont('Consolas', 12))

        self.getcode()
        
        button = QPushButton('종료', self)
        button.setToolTip('example')
        button.move(280, 360)
        button.clicked.connect(QCoreApplication.instance().quit)
        self.show()

    def getnum(self, code):
        if code == 'seperate':
            i, okPressed = QInputDialog.getInt(self, "점심 조별 인원수 정하기!", "여자 조별 인원수 :", 4, 2, 4, 1)
            if okPressed:
                self.getnum2(code, i)
                
        else:
            i, okPressed = QInputDialog.getInt(self, "점심 조별 인원수 정하기!", "조별 인원수 :", 4, 2, 4, 1)
            self.random_meal(code, i)
                
    def getnum2(self, code, n):
        i, okPressed = QInputDialog.getInt(self, "점심 조별 인원수 정하기!", "남자 조별 인원수 :", 4, 0, 10, 1)
        if okPressed:
            self.random_meal(code, n, i)
        
    def getcode(self):
        items = {'random', 'seperate', 'balance'}
        i, okPressed = QInputDialog.getItem(self, "버전 정하기!", "버전 코드 :", items)
        if okPressed:
            self.getnum(i)
    
    def random_meal(self, code, *n):
        team = random_lunch.random_lunch(code, *n)
        cnt = 1
        message = ''
        for i in team:
            message = message + 'team' + str(cnt) + ' : ' + str(i) + '\n\n'
            cnt += 1
        
        self.textbox.setText(message)
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
