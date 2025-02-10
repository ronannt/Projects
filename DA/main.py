import sys
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem

myDir = os.getcwd()
sys.path.append(myDir)
app = QtWidgets.QApplication([])

login = uic.loadUi("DA\\Frame\\login.ui")

login.show()
app.exec_()