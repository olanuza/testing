#Exercise 2

from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 400, 25)

        self.startbtn = QPushButton('Start', self)
        self.startbtn.move(30, 80)
        self.startbtn.clicked.connect(self.pushStart)

        self.stopbtn = QPushButton('Stop', self)
        self.stopbtn.move(320, 80)
        self.stopbtn.clicked.connect(self.pushStop)
        
        self.setGeometry(300, 300, 430, 170)
        self.setWindowTitle('This is a 5s timer. Press stop to abort')
        self.show()
        
        
    def timerEvent(self, e):
      
        if self.step >= 100:
            
            self.timer.stop()
            self.killTimer(self.timer.timerId())
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        

    def pushStart(self):
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(50,self)
            
    def pushStop(self):
        self.timer.stop()
        self.pbar.setValue(0)
        self.killTimer(self.timer.timerId())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())