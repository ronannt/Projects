import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import mysql.connector
from mysql.connector import errorcode
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem


class Primary_Functions:
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
            self.conn = mysql.connector.connect(host='localhost', user=user, password=password, database='crud_database_1')
            print("Database connection made!")
            self.cursor = self.conn.cursor()
            login.close()
            frame.show()
            Primary_Functions.Update(Primary_Functions, frame)
        except mysql.connector.Error as error:
                Primary_Functions.Error(Primary_Functions, error, login)
                return

    def ClosePopUp(self, frame):
        frame.frame_erro.hide()

    def Update(self, frame):
        try:
            q = ("SELECT * FROM dms_database")
            self.cursor.execute(q)
            result = self.cursor.fetchall()
            frame.table.setRowCount(0)
            for row_number, row_data in enumerate(result):
                frame.table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    frame.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mysql.connector.Error as error:
                Primary_Functions.Error(Primary_Functions, error, frame)
                return

    def Filter(self, frame, status):
        if status == 'None':
            frame.label_erro.setText("Please select a Filter!")
            frame.frame_erro.show()
            return
        else:
            try:
                q = (f"SELECT * FROM dms_database WHERE status = '{status}';")
                self.cursor.execute(q)
                result = self.cursor.fetchall()
                frame.table.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    frame.table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        frame.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            except mysql.connector.Error as error:
                Primary_Functions.Error(Primary_Functions, error, frame)
                return
        

    def Create(self, group, protocol, st1, st2, st3, frame, home):
        if st1.isChecked():
            status = ('Started')
            ck = 1
        elif st2.isChecked():
            status = ('Analyzing')
            ck = 2
        elif st3.isChecked():
            status = ('Finished')
            ck = 3
        else:
            frame.label_erro.setText("Please select Status!")
            frame.frame_erro.show()
            return
        
        if protocol == '':
            frame.label_erro.setText("Please enter Protocol!")
            frame.frame_erro.show()
            return
        elif protocol.isnumeric() == False:
            frame.label_erro.setText("Only numbers in the protocol!")
            frame.frame_erro.show()
            return
        elif len(protocol) > 10:
            frame.label_erro.setText("Protocol max 10 numbers!")
            frame.frame_erro.show()
            return
        
        group_items = group.selectedItems()
        group_texts = [item.text() for item in group_items]
        try:
            groupf = group_texts[0]
        except IndexError:
            frame.label_erro.setText('Please select Group!')
            frame.frame_erro.show()
            return

        try:
            q = "INSERT INTO `dms_database` (`id`, `group`, `protocol`, `status`) VALUES (NULL, %s, %s, %s);"
            self.cursor.execute(q, (groupf, protocol, status))
            self.conn.commit()
            frame.list_group.clearSelection()
            frame.line_protocol.clear()
            if ck == 1:
                st1.setAutoExclusive(False)
                st1.setChecked(False)
                st1.setAutoExclusive(True)
            elif ck == 2:
                st2.setAutoExclusive(False)
                st2.setChecked(False)
                st2.setAutoExclusive(True)
            elif ck ==31:
                st3.setAutoExclusive(False)
                st3.setChecked(False)
                st3.setAutoExclusive(True)
            frame.frame_erro.hide()
            frame.close()
            Primary_Functions.Update(Primary_Functions, home)
        except mysql.connector.Error as error:
                Primary_Functions.Error(Primary_Functions, error, frame)
                return
            
    def Delete(self, id, delete, frame):
        if id == '':
            delete.label_erro.setText("Please enter ID!")
            delete.frame_erro.show()
            return
        elif id.isnumeric() == False:
            delete.label_erro.setText("Only numbers in the ID!")
            delete.frame_erro.show()
            return
        elif len(id) > 10:
            delete.label_erro.setText("ID max 10 numbers!")
            delete.frame_erro.show()
            return
        
        try:
            q = (f"DELETE FROM `dms_database` WHERE `dms_database`.`id` = {id};")
            self.cursor.execute(q)
            self.conn.commit()
            delete.line_id.clear()
            delete.frame_erro.hide()
            delete.close()
            Primary_Functions.Update(Primary_Functions, frame)
        except mysql.connector.Error as error:
                Primary_Functions.Error(Primary_Functions, error, delete)
                return

    def ShowFrame(self, frame):
        frame.show()

    def Close(self, frame):
        frame.close()
        self.cursor.close()
        self.conn.close()
        print('Connection closed!')