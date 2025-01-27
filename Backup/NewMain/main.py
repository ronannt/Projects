import sys
import os
import PyQt5
import file_rc
import shutil
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from funcs import Funcs
from win32com.client import Dispatch

myDir = os.getcwd()
sys.path.append(myDir)
app = QtWidgets.QApplication([])

cod = "nada"

def get_version_via_com(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

if __name__ == "__main__":

    paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
    verfor = int(version[2])

    pypath = sys.executable
    n = 10
    dest = pypath[:-n]
    dest2 = f"{myDir}\\ChromeDrivers\\"

    print(f"Caminho de destino: {dest}")

    if verfor == 9:
        print("Versão 109")
        scr = f"{myDir}\\ChromeDrivers\\109\\chromedriver.exe"
        shutil.copy(scr, dest2)
    elif verfor == 0:
        print("Versão Chrome 110")
        scr = f"{myDir}\\ChromeDrivers\\110\\chromedriver.exe"
        shutil.copy(scr, dest2)

    elif verfor == 1:
        print("Versão 111")
        scr = f"{myDir}\\ChromeDrivers\\111\\chromedriver.exe"
        shutil.copy(scr, dest2)
    else:
        print("Versão do Navegador Chrome divergente dos Drivers!")

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('Sem privilégios suficientes. Reiniciando...')
        ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    else:
        print('Privilégios superiores garantidos')

    scr2 = f"{myDir}\\ChromeDrivers\\chromedriver.exe"
    try:
        shutil.move(scr2, dest)
        print("Pasta copiada.")
    except:
        print("Pasta ja existe.")

#Carregamento de telas
login = uic.loadUi("login.ui")
sgbd_home = uic.loadUi("sgbd.ui")
tp_proj = uic.loadUi("tpprojeto.ui")
ep_home = uic.loadUi("easy_project_home.ui")

#Login
login.frame_erro.hide()
login.bt_cl_popup.clicked.connect(lambda: Funcs.ClosePopUp(login))
login.bt_enter_login.clicked.connect(lambda: Funcs.Login(Funcs, login.line_user.text(), login.line_pass.text(), login, sgbd_home))

#SGBD Home
sgbd_home.frame_erro.hide()
sgbd_home.bt_cl_popup.clicked.connect(lambda: Funcs.ClosePopUp(sgbd_home))
sgbd_home.bt_add.clicked.connect(lambda: Funcs.ShowWindow(tp_proj))

#Tipo de projeto
tp_proj.frame_erro.hide()
tp_proj.bt_cl_popup.clicked.connect(lambda: Funcs.ClosePopUp(tp_proj))
tp_proj.okbt.clicked.connect(lambda: Funcs.TipoPessoa(tp_proj.radio_fisica, tp_proj.radio_juridica, tp_proj.radio_10kw, tp_proj.radio_75kw, ep_home, tp_proj))

#Easy Project Home Pessoa Juridica
ep_home.frame_erro.hide()
ep_home.inv63a.hide()
ep_home.inv100a.hide()
ep_home.inv70a.hide()
ep_home.bt_cl_popup.clicked.connect(lambda: Funcs.ClosePopUp(ep_home))

ep_home.bt_mono.clicked.connect(lambda: Funcs.monofa(ep_home))
ep_home.bt_bi.clicked.connect(lambda: Funcs.bifa(ep_home))
ep_home.bt_tri.clicked.connect(lambda: Funcs.trifa(ep_home))

ep_home.okbt.clicked.connect(lambda: Funcs.Criar(
        ep_home.linetituc.text(),
        ep_home.lineuc.text(),
        ep_home.linecnc.text(),
        ep_home.linerg.text(),
        ep_home.linecpfcnpj.text(),
        ep_home.linerua.text(),
        ep_home.linenum.text(),
        ep_home.linecomp.text(),
        ep_home.linebairro.text(),
        ep_home.linecid.text(),
        ep_home.linecep.text(),
        ep_home.linedisjuntor.text(),
        ep_home.linecla.text(),
        ep_home.lineqtdmod.text(),
        ep_home.linefabmod.text(),
        ep_home.linemodmod.text(),
        ep_home.lineareaarranjo.text(),
        ep_home.lineqtdinversor.text(),
        ep_home.linefabinversor.text(),
        ep_home.linemodinversor.text(),
        ep_home.linesomamod.text(),
        ep_home.linesomainversor.text(),
        ep_home.linelttd.text(),
        ep_home.linelgtd.text(),
        ep_home.linecargainsta.text(),
        ep_home.linecargainstagera.text(),
        ep_home.linetensao.text(),
        ep_home.linedataprev.text(),
        ep_home.linetpatvd.text(),
        ep_home.linedisjuntor2.text(),
        ep_home.lineptnmod.text(),
        ep_home.lineqtdarranjo.text(),
        ep_home.lineseriearranjo.text(),
        ep_home.lineptninversor.text(),
        ep_home.lineqtdentinversor.text(),
        ep_home.lineespcc.text(),
        ep_home.lineespca.text(),
        ep_home,
        ep_home.listpot,
        ep_home.listpot2,
        ep_home.inv63a,
        ep_home.inv100a,
        ep_home.inv70a,
        ep_home.lineempresa.text(),
        ep_home.linecnpj.text()))

login.show()
app.exec_()