import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import mysql.connector
from mysql.connector import errorcode
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem


class Functions:
    def Error(self, error, frame):
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            frame.label_erro.setText("Server not available!")
            frame.frame_erro.show()
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            frame.label_erro.setText("Wrong Password or User!")
            frame.frame_erro.show()
        else:
            print(error)
            frame.label_erro.setText('Unknow error!')
            frame.frame_erro.show()
            return
        
    def Login(self, user, password, frame, login):
        try:
            self.conn = mysql.connector.connect(host='localhost', user=user, password=password, database='auto_doc')
            print("Database connection made!")
            self.cursor = self.conn.cursor()
            login.close()
            frame.show()
            Functions.Update(Functions, frame)
        except mysql.connector.Error as error:
                Functions.Error(Functions, error, login)
                return