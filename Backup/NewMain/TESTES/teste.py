import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
import file_rc

def ClosePopUp(window):
    window.frame_erro.hide()
def monofa(home):
        home.rd1.hide()
        home.rd2.hide()
        home.rd3.show()
def bifa(home):
        home.rd1.show()
        home.rd2.show()
        home.rd3.hide()


app = QtWidgets.QApplication([])

#HOME
home = uic.loadUi("teste.ui")
home.frame_erro.hide()
home.rd1.hide()
home.rd2.hide()
home.rd3.hide()
home.bt_cl_popup.clicked.connect(lambda: ClosePopUp(home))
home.bt1.clicked.connect(lambda: monofa(home))
home.bt2.clicked.connect(lambda: bifa(home))

home.show()
app.exec_()