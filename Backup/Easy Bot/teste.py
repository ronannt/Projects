from __future__ import annotations
import sys
import os
import docx
from docx import Document
from openpyxl import *
from datetime import date
import shutil
from docx.shared import Inches
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
import time
import pyautogui
from selenium import webdriver
from win32com.client import Dispatch
import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
myDir = os.getcwd()
sys.path.append(myDir)
home_directory = os.path.expanduser( '~' )


class functions:
    def Formulario10KW(nome, cpf, rua, numero, bairro, cidade, cep, uc, classe, lttd, lgtd, cargainsta, cargainstagera, tensao):
        data = date.today()
        curdate = data.strftime('%d/%m/%Y')
        wb = load_workbook(f"{myDir}/Forms/formularioEXL.xlsx")
        sh = wb['MICROGERAÇÃO <= 10KW']
        sh['F5'] = nome
        sh['F4'] = uc
        sh['U4'] = classe
        sh['F10'] = cpf
        sh['F6'] = rua
        sh['AC6'] = cep
        sh['U7'] = cidade
        sh['X6'] = numero
        sh['F7'] = bairro
        sh['R12'] = lttd
        sh['AB12'] = lgtd
        sh['I13'] = cargainsta
        sh['L16'] = cargainstagera
        sh['V13'] = tensao
        sh['M38'] = curdate

        newf = f"{home_directory}/Desktop/{nome}"
        os.mkdir(newf)
        wb.save(filename=f"Formulario{uc}.xlsx")
        scr = f"Formulario{uc}.xlsx"
        dest = f"{home_directory}/Desktop/{nome}"
        shutil.move(scr, dest)