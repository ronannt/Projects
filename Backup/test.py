import sys
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem


def ShowwData(data):
    print(str(data.toPyDate()))

myDir = os.getcwd()
sys.path.append(myDir)
app = QtWidgets.QApplication([])

test = uic.loadUi("RegistrationSystem/Frames/test.ui")
test.calendar.setGridVisible(True);
test.calendar.setVerticalHeaderFormat(test.calendar.NoVerticalHeader)
test.calendar.selectionChanged.connect(lambda: ShowwData(test.calendar.selectedDate()))

test.show()
app.exec_()
