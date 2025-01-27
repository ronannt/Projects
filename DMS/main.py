import sys
import os
from Functions import Primary_Functions
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem

myDir = os.getcwd()
sys.path.append(myDir)
app = QtWidgets.QApplication([])

login = uic.loadUi("Frames\\login.ui")
home = uic.loadUi("Frames\\sgbd.ui")
add = uic.loadUi("Frames\\add.ui")
delete = uic.loadUi("Frames\\del.ui")

login.setWindowIcon(QtGui.QIcon('Icons\\login.png'))
home.setWindowIcon(QtGui.QIcon('Icons\\login.png'))
add.setWindowIcon(QtGui.QIcon('Icons\\login.png'))
delete.setWindowIcon(QtGui.QIcon('Icons\\login.png'))

login.frame_erro.hide()
login.bt_cl_popup.clicked.connect(lambda: Primary_Functions.ClosePopUp(Primary_Functions, login))
login.bt_enter_login.clicked.connect(lambda: Primary_Functions.Login(Primary_Functions, login.line_user.text(), login.line_pass.text(), home, login))

home.frame_erro.hide()
home.bt_cl_popup.clicked.connect(lambda: Primary_Functions.ClosePopUp(Primary_Functions, home))
home.bt_add.clicked.connect(lambda: Primary_Functions.ShowFrame(Primary_Functions, add))
home.bt_refresh.clicked.connect(lambda: Primary_Functions.Update(Primary_Functions, home))
home.bt_filter.clicked.connect(lambda: Primary_Functions.Filter(Primary_Functions, home, home.status_box.currentText()))
home.bt_exit.clicked.connect(lambda: Primary_Functions.Close(Primary_Functions, home))
home.bt_delete.clicked.connect(lambda: Primary_Functions.ShowFrame(Primary_Functions, delete))

add.frame_erro.hide()
add.bt_cl_popup.clicked.connect(lambda: Primary_Functions.ClosePopUp(Primary_Functions, add))
add.bt_add.clicked.connect(lambda: Primary_Functions.Create(Primary_Functions, add.list_group, add.line_protocol.text(), add.ck_started, add.ck_analyzing, add.ck_finished, add, home))

delete.frame_erro.hide()
delete.bt_cl_popup.clicked.connect(lambda: Primary_Functions.ClosePopUp(Primary_Functions, delete))
delete.bt_del.clicked.connect(lambda: Primary_Functions.Delete(Primary_Functions, delete.line_id.text(), delete, home))

login.show()
app.exec_()