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
    def __init__(self, arg1, arg2):
        super().__init__(arg1, arg2)
        self.x = 1920
        self.y = 1080
        
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
        self.xlist = []
        self.ylist = []
        self.vxlist= []
        self.vylist = []
        for i in range(20):
            x,y=random.randrange(self.win_width), random.randrange(self.win_height)
            btn = FlyingButton('',self)
            btn.resize(20,20)
            btn.move(x,y)
            color = 'red', 'yellow','blue','purple','black'
            colors = random.choice(color)           
            btn.setStyleSheet(f"background-color:{colors}")
            btn.clicked.connect(self.callback)
            self.btns.append(btn)
            self.xlist.append(x)
            self.ylist.append(y)
            self.vxlist.append(10)
            self.vylist.append(10)
        self.run_timer.timeout.connect(self.update)
        self.run_timer.start(self.delta_t)
        self.show()

    def update(self):
        for i in range(len(self.btns)):
            self.xlist[i] += self.vxlist[i]
            self.ylist[i] += self.vylist[i]
            self.btns[i].move(self.xlist[i],self.ylist[i])
            if self.xlist[i] >= self.win_width - self.vx:
                self.vxlist[i] = -self.vxlist[i]
            if self.ylist[i] >= self.win_height - self.vy:
                self.vylist[i] = -self.vylist[i]                          
            if self.ylist[i] <= 0:
                self.vylist[i] = -self.vylist[i]
            if self.xlist[i] <= 0:
               self.vxlist[i] = -self.vxlist[i]
            

    def btnrand(self):

        pass

        #self.show()
    def callback(self):
        self.counter += 1
        print(self.counter)        



if __name__ == "__main__":

    app = QApplication(sys.argv)
    an = Animation()
    sys.exit(app.exec())