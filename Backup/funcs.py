import sys
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
import time
import mysql.connector
from mysql.connector import errorcode
myDir = os.getcwd()
sys.path.append(myDir)


class Funcs:
    user = ""
    def ClosePopUp(window):
        window.frame_erro.hide()
    def ShowWindow(self, wind):
        wind.show()

    def Login(self, userget, paswget, login, wind):
        global user
        try:
            self.db_connection = mysql.connector.connect(host='localhost', user=userget, password=paswget, database='test')
            print("Banco de dados conectado!")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                login.label_erro.setText("Servidor não disponivel!")
                login.frame_erro.show()
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                login.label_erro.setText("Usuário e senha inválido!")
                login.frame_erro.show()
            else:
                login.label_erro.setText("Erro desconhecido!")
                login.frame_erro.show()
                print(error)
        else:
                print("Conectado!")
                login.close()
                Funcs.UpdateTable(Funcs, wind)
                wind.show()
                user = userget

    def UpdateTable(self, wind):
        self.cursor = self.db_connection.cursor()
        q = ("SELECT codigo, responsavel, status, obs FROM test.customers WHERE 1;")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table = wind.table
        table.setRowCount(len(result))
        table.setColumnCount(4)
        for i in range(0, len(result)):
            for j in range(0, 4):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
        wind.show()
        self.cursor.close()

    def NewData(self, nome, rg, cpf, nascimento, endereco, cidade, estado, celular, email, obs, add):
        data = str(nascimento.toPyDate())
        vartext = [nome, endereco, cidade, estado, email, obs]
        varnumber = [rg, cpf, celular]
        vartextf = []
        varnumberf = []

        for var in vartext:
            if var == "":
                add.label_erro.setText("Dados inválidos, verifique!")
                add.frame_erro.show()
            varf = ""
            for i in var:
                if i.isalnum():
                    varf += i
            varf.lower()
            vartextf.append(varf)

        for var in varnumber:
            if var == "":
                add.label_erro.setText("Dados inválidos, verifique!")
                add.frame_erro.show()
            varf = ""
            for i in var:
                if i.isnumeric():
                    varf += i
            varf.lower()
            varnumberf.append(varf)

        self.cursor = self.db_connection.cursor()
        q = (f"INSERT INTO test.customers (responsavel, status, obs, nome, rg, cpf, nascimento, endereco, cidade, estado, celular, email) VALUES ('{user}', 'Documentação', '{vartextf[5]}', '{vartextf[0]}', '{varnumberf[0]}', '{varnumberf[1]}', '{data}', '{vartextf[1]}', '{vartextf[2]}', '{vartextf[3]}', '{varnumberf[2]}', '{vartextf[4]}');")
        self.cursor.execute(q)
        self.db_connection.commit()
        self.cursor.close()

        #Funcs.ClearAdd(Funcs, setor, add, status1, status2, status3)
        add.close()