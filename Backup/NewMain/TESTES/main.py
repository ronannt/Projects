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

app = QtWidgets.QApplication([])

#HOME
home = uic.loadUi("sgbd.ui")

db = mysql.connector.connect(host='localhost', user='root', password='', database='ntc_clientes')
print("Banco de dados conectado!")
cursor = db.cursor()
cursor.execute("SELECT * FROM ntc_clientes.Clientes;")
result = cursor.fetchall()
table = home.table
table.setRowCount(len(result))
table.setColumnCount(4)
home.bt_att.hide()
for i in range(0, len(result)):
    for j in range(0, 4):
        table.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))


home.show()
app.exec_()