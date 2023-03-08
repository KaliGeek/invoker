import sys
import time
import threading
from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDesktopWidget, QInputDialog,  QAction, QApplication, QLabel
import random
class FlyingButton(QPushButton):
    def __init__(self, arg1, arg2,arg3,arg4):
        super().__init__(arg1, arg2)
        self.x = 1920
        self.y = 1080
        self.win_width = arg3
        self.win_height = arg4
    def setpos(self,x,y):
        self.x = x
        self.y = y
    def setv(self,vx,vy):
        self.vx = vx
        self.vy = vy
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.move(self.x,self.y)
        if self.x >= self.win_width - self.vx:
                self.vx = -self.vx
        if self.y >= self.win_height - self.vy:
                self.vy = -self.vy                          
        if self.y <= 0:
                self.vy = -self.vy
        if self.x <= 0:
               self.vx = -self.vx        
class Animation(QWidget):

    def __init__(self, rows = 40, cols = 40):
        self.win_width = 1920
        self.win_height = 1080
        self.vx = 10
        self.vy = 10 
        self.run_timer = QTimer()
        self.delta_t = 200
        self.counter = 0
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, self.win_width, self.win_height)
        self.btns = [] 
        for i in range(20):
            x,y=random.randrange(self.win_width), random.randrange(self.win_height)
            btn = FlyingButton('',self,self.win_width, self.win_height)
            btn.resize(20,20)
            btn.move(x,y)
            color = 'red', 'yellow','blue','purple','black'
            colors = random.choice(color)           
            btn.setStyleSheet(f"background-color:{colors}")
            btn.clicked.connect(self.callback)
            self.btns.append(btn)
            btn.setpos(x,y)
            btn.setv(random.randrange(10,50),random.randrange(10,50))
        self.run_timer.timeout.connect(self.update)
        self.run_timer.start(self.delta_t)
        self.show()

    def update(self):
        for i in range(len(self.btns)):
            self.btns[i].update()            

    def btnrand(self):

        pass

        #self.show()
    def callback(self):
        self.counter += 1
        print(self.counter)        








#commitgittest232234234234
#wasser
if __name__ == "__main__":

    app = QApplication(sys.argv)
    an = Animation()
    sys.exit(app.exec())