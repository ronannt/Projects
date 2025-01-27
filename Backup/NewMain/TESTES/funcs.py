import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem


class Funcs:

    def ClosePopUp(window):
        window.frame_erro.hide()

    def Login(self, userget, paswget, login, home):
        try:
            self.db_connection = mysql.connector.connect(host='localhost', user=userget, password=paswget, database='test_db')
            print("Banco de dados conectado!")
            self.cursor = self.db_connection.cursor()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                login.label_erro.setText("Servidor não disponivel!")
                login.frame_erro.show()
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                login.label_erro.setText("Usuário e senha inválido!")
                login.frame_erro.show()
            else:
                login.label_erro.setText("\erro desconhecido!")
                login.frame_erro.show()
                print(error)
        else:
                print("Conectado!")
                #home.show()
                login.close()
                home.show()
                
            #VENDEDOR
            self.cursor.execute(f"SELECT * FROM db.uservendas WHERE users = '{userget}';")
            if self.cursor.fetchone():
                q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{userget}'")
                self.cursor.execute(q)
                result = self.cursor.fetchall()
                table_projetos = homevendedor.tabelavendedor
                table_projetos.setRowCount(len(result))
                table_projetos.setColumnCount(6)
                for i in range(0, len(result)):
                    for j in range(0, 6):
                        table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
                homevendedor.show()
                login.close()
                idnew = 2
                #HomeShowVendas()
            user = userget
            #PROJETISTA
            self.cursor.execute(f"SELECT * FROM db.userprojetos WHERE users = '{userget}';")
            if self.cursor.fetchone():
                q = (f"SELECT * FROM db.projetos WHERE projetista = '{userget}'")
                self.cursor.execute(q)
                result = self.cursor.fetchall()
                table_projetos = homeprojetista.tabelaprojetos
                table_projetos.setRowCount(len(result))
                table_projetos.setColumnCount(6)
                for i in range(0, len(result)):
                    for j in range(0, 6):
                        table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
                homeprojetista.show()
                login.close()
                idnew = 3
            user = userget
    def Select(self, tabela, Lid, Lcliente, Luc, Lprotocolo, Lcriacao, Ldoc, Lproc, Lconta, Lkit, Lcnc, Lenvana, Laprana, Lenvvis, Laprvis, Lenvtro, Laprtro, Lprocesso, Lobs, Lcpfcnpj, Lcep, Lnumero, Lprvconc, Lcarga, info):
        tabela.currentItem()
        cod = tabela.currentItem().text()
        self.cursor.execute(f"SELECT * FROM db.datainfo WHERE id = '{cod}';")
        result = self.cursor.fetchall()

        id = [x[0] for x in result]
        cliente = [x[1] for x in result]
        uc = [x[2] for x in result]
        protocolo = [x[3] for x in result]
        criacao = [x[4] for x in result]
        doc = [x[5] for x in result]
        proc = [x[6] for x in result]
        conta = [x[7] for x in result]
        kit = [x[8] for x in result]
        cnc = [x[9] for x in result]
        envana = [x[10] for x in result]
        aprana = [x[11] for x in result]
        envvis = [x[12] for x in result]
        aprvis = [x[13] for x in result]
        envtro = [x[14] for x in result]
        aprtro = [x[15] for x in result]
        processo = [x[16] for x in result]
        obs = [x[17] for x in result]
        cpfcnpj = [x[18] for x in result]
        cep = [x[19] for x in result]
        numero = [x[20] for x in result]
        prvconc = [x[21] for x in result]
        carga = [x[22] for x in result]


        clientef = (cliente[0])
        ucf = (uc[0])
        protocolof = (protocolo[0])
        criacaof = (criacao[0])
        docf = (doc[0])
        procf = (proc[0])
        contaf = (conta[0])
        kitf = (kit[0])
        cncf = (cnc[0])
        envanaf = (envana[0])
        apranaf = (aprana[0])
        envvisf = (envvis[0])
        aprvisf = (aprvis[0])
        envtrof = (envtro[0])
        aprtrof = (aprtro[0])
        processof = (processo[0])
        obsf = (obs[0])
        cpfcnpjf = (cpfcnpj[0])
        cepf = (cep[0])
        numerof = (numero[0])
        prvconcf = (prvconc[0])
        cargaf = (carga[0])
        info.show()
        Lid.setText(f"ID: {id}")
        Lcliente.setText(f"Cliente: {clientef}")
        Luc.setText(f"UC: {ucf}")
        Lprotocolo.setText(f"Protocolo: {protocolof}")
        Lcriacao.setText(f"Criado em: {criacaof}")
        Ldoc.setText(f"Documento adicionado em: {docf}")
        Lproc.setText(f"Procuração adicionada em: {procf}")
        Lconta.setText(f"Conta adicionada em: {contaf}")
        Lkit.setText(f"kit adicionado em: {kitf}")
        Lcnc.setText(f"Concessionária: {cncf}")
        Lenvana.setText(f"Envio da análise: {envanaf}")
        Laprana.setText(f"Aprovação da análise: {apranaf}")
        Lenvvis.setText(f"Envio da vistoria: {envvisf}")
        Laprvis.setText(f"Aprovação da vistoria: {aprvisf}")
        Lenvtro.setText(f"Envio da troca do medidor: {envtrof}")
        Laprtro.setText(f"Trocado em: {aprtrof}")
        Lprocesso.setText(f"Processo: {processof}")
        Lobs.setText(f"Obs: {obsf}")
        Lcpfcnpj.setText(f"CPF/CNPJ: {cpfcnpjf}")
        Lcep.setText(f"CEP: {cepf}")
        Lnumero.setText(f"Numero: {numerof}")
        Lprvconc.setText(f"Previsão de troca: {prvconcf}")
        Lcarga.setText(f"Carga: {cargaf}")
    def CriarCliente(self, nome, cpfcnpj, cep, numero, uc, cnc, sim, nao, obs, carga, alertnewclient, newclient):
        prot = 0
        processo = ("Documentação")

        if nome == "":
            alertnewclient.show()
        else:
            nomef = ""
            for i in nome:
                if i.isalnum() or i == " ":
                    nomef += i

            if cpfcnpj == "":
                cpfcnpj = "0"
            cpfcnpjf = ""
            for i in cpfcnpj:
                if i.isalnum() or i == " ":
                    cpfcnpjf += i

            if cep == "":
                cep = "0"
            cepf = ""
            for i in cep:
                if i.isalnum() or i == " ":
                    cepf += i

            if numero == "":
                numero = "0"
            numerof = ""
            for i in numero:
                if i.isalnum() or i == " ":
                    numerof += i

            if uc == "":
                uc = "0"
            ucf = ""
            for i in uc:
                if i.isalnum() or i == " ":
                    ucf += i

            if cnc == "":
                cnc = "N"
            cncf = ""
            for i in cnc:
                if i.isalnum() or i == " ":
                    cncf += i
            cncf.upper()

            if obs == "":
                obs = "N"
            obsf = ""
            for i in obs:
                if i.isalnum() or i == " ":
                    obsf += i

            if carga == "":
                carga = "0"
            cargaf = ""
            for i in carga:
                if i.isalnum() or i == " ":
                    cargaf += i

            if sim.isChecked():
                processo = ("Documentação")
                self.cursor.execute("SELECT MAX(id) as maxId FROM db.datainfo;")
                result = self.cursor.fetchone()
                newid = (result[0] + 1)
                self.cursor.execute(
                    f"INSERT INTO db.info VALUES ('{newid}', '{nomef}', '{ucf}', '{prot}', '{cnc}', '{processo}', '{obsf}', '{cpfcnpjf}', '{cepf}', '{numerof}', '{cargaf}', '{self.user}');")
                self.cursor.execute(
                    f"INSERT INTO db.datainfo (id, cliente, uc, protocolo, criacao, cnc, processo, obs, cpf, cep, numero, carga, vendedor) VALUES ('{newid}', '{nomef}', '{ucf}', '{prot}', CURDATE(), '{cnc}', '{processo}', '{obsf}', '{cpfcnpjf}', '{cepf}', '{numerof}', '{cargaf}', '{self.user}');")
                self.cursor.execute(
                    f"INSERT INTO db.clientesvendas (id, cliente, protocolo, cnc, Processo, obs, vendedor) VALUES ('{newid}', '{nomef}', '{prot}', '{cnc}', '{processo}', '{obsf}', '{self.user}')")
                self.cursor.execute(
                    f"INSERT INTO db.projetos (id, cliente, protocolo, cnc, processo, obs, projetista) VALUES ('{newid}', '{nomef}', '{prot}', '{cnc}', '{processo}', '{obsf}', 'vitor')")
                self.db_connection.commit()
                Funcs.ClearLine(Funcs, newclient)
                #Funcs.EnvAnexo(Funcs, newid)

            if nao.isChecked():
                processo = ("Criação de Projeto")
                self.cursor.execute("SELECT MAX(id) as maxId FROM db.datainfo;")
                result = self.cursor.fetchone()
                newid = (result[0] + 1)
                self.cursor.execute(
                    f"INSERT INTO db.info VALUES ('{newid}', '{nomef}', '{ucf}', '{prot}', '{cnc}', '{processo}', '{obsf}', '{cpfcnpjf}', '{cepf}', '{numerof}', '{cargaf}', '{self.user}');")
                self.cursor.execute(
                    f"INSERT INTO db.datainfo (id, cliente, uc, protocolo, criacao, cnc, processo, obs, cpf, cep, numero, carga, vendedor) VALUES ('{newid}', '{nomef}', '{ucf}', '{prot}', CURDATE(), '{cnc}', '{processo}', '{obsf}', '{cpfcnpjf}', '{cepf}', '{numerof}', '{cargaf}', '{self.user}');")
                self.cursor.execute(
                    f"INSERT INTO db.clientesvendas (id, cliente, protocolo, cnc, Processo, obs, vendedor) VALUES ('{newid}', '{nomef}', '{prot}', '{cnc}', '{processo}', '{obsf}', '{self.user}');")
                self.cursor.execute(
                    f"INSERTO INTO db.projetos (id, cliente, protocolo, cnc, processo, obs, projetista) VALUES ('{newid}', '{nomef}', '{prot}', '{cnc}', '{processo}', '{obsf}', 'vitor')")
                self.db_connection.commit()
                Funcs.ClearLine(Funcs, newclient)
            if idnew == 1:
                Funcs.ShowADM(Funcs, homef)
                newclient.close()
            elif idnew == 2:
                Funcs.ShowVendedor(Funcs, homevendedorf)
                newclient.close()
            else:
                newclient.close()
    def ShowVendedor(self, homevendedor):
        q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{self.user}'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homevendedor.tabelavendedor
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def ShowProjetista(self, homeprojetista):
        q = (f"SELECT * FROM db.projetos WHERE projetista = '{self.user}'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homeprojetista.tabelaprojetos
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def ShowADM(self, home):
        q = (f"SELECT * FROM db.clientesvendas")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = home.table_adm
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def Delete(self, tabela, alertidupdate, excluir):
        tabela.currentItem()
        idcode = tabela.currentItem().text()
        if idcode == None:
            alertidupdate.show()
        else:
            cod = ""
            for i in idcode:
                if i.isnumeric() or i == " ":
                    cod += i
            self.cursor.execute(f'DELETE FROM db.info WHERE id = {cod};')
            self.cursor.execute(f'DELETE FROM db.datainfo WHERE id = {cod};')
            self.cursor.execute(f'DELETE FROM db.clientesvendas WHERE id = {cod};')
            self.cursor.execute(f'DELETE FROM db.projetos WHERE id = {cod};')
            self.db_connection.commit()
            if idnew == 1:
                Funcs.ShowADM(Funcs, homef)
                CloseExcluir(excluir)
            if idnew == 2:
                Funcs.ShowVendedor(Funcs, homevendedorf)
                CloseExcluir2(excluir)
            if idnew == 3:
                Funcs.ShowProjetista(Funcs, homeprojetistaf)
                CloseExcluir3(excluir)
            else:
                print("ERROR_idexc_DEFAULT")
                CloseExcluir(excluir)
                CloseExcluir2(excluir)
                CloseExcluir3(excluir)
    def UpdateV(self, tabela, nome, cpf, cep, numero, cnc, carga, uc, alertidupdate, att2, homevendedor):
        tabela.currentItem()
        idcode = tabela.currentItem().text()
        if idcode == "":
            alertidupdate.show()
        else:
            cod = ""
            for i in idcode:
                if i.isnumeric() or i == " ":
                    cod += i
            # NOME
            if nome == None:
                nomes = 1
            else:
                nomef = ""
                for i in nome:
                    if i.isalpha() or i == " ":
                        nomef += i
                self.cursor.execute(f"UPDATE db.info SET cliente = '{nomef}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cliente = '{nomef}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET cliente = '{nomef}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET cliente = '{nomef}' WHERE id = {cod};")
                self.db_connection.commit()
                nomes = 11
            # CPF
            if cpf == "":
                cpfs = 2
            else:
                cpfcnpj = ""
                for i in cpf:
                    if i.isnumeric() or i == " ":
                        cpfcnpj += i
                self.cursor.execute(f"UPDATE db.info SET cpf = {cpfcnpj} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cpf = {cpfcnpj} WHERE id = {cod};")
                self.db_connection.commit()
                cpfs = 22
            # CEP
            if cep == "":
                ceps = 3
            else:
                cepf = ""
                for i in cep:
                    if i.isalnum() or i == " ":
                        cepf += i
                self.cursor.execute(f"UPDATE db.info SET cep = {cepf} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cep = {cepf} WHERE id = {cod};")
                self.db_connection.commit()
                ceps = 33
            # NUMERO
            if numero == "":
                numeros = 4
            else:
                numerof = ""
                for i in numero:
                    if i.isalnum() or i == " ":
                        numerof += i
                self.cursor.execute(f"UPDATE db.info SET numero = {numerof} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET numero = {numerof} WHERE id = {cod};")
                self.db_connection.commit()
                numeros = 44
            # CNC
            if cnc == "":
                cncs = 6
            else:
                cncf = ""
                for i in cnc:
                    if i.isalnum() or i == " ":
                        cncf += i
                self.cursor.execute(f"UPDATE db.info SET cnc = '{cncf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cnc = '{cncf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET cnc = '{cncf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET cnc = '{cncf}' WHERE id = {cod};")
                self.db_connection.commit()
                cncs = 66
            # CARGA
            if carga == "":
                cargas = 7
            else:
                cargaf = ""
                for i in carga:
                    if i.isalnum() or i == " ":
                        cargaf += i
                self.cursor.execute(f"UPDATE db.info SET carga = {cargaf} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET carga = {cargaf} WHERE id = {cod};")
                self.db_connection.commit()
                cargas = 77
            # UC
            if uc == "":
                ucs = 5
            else:
                ucf = ""
                for i in uc:
                    if i.isnumeric() or i == " ":
                        ucf += i
                self.cursor.execute(f"UPDATE db.info SET uc = {ucf} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET uc = {ucf} WHERE id = {cod};")
                self.db_connection.commit()
                ucs = 55
            #Funcs.EnvAnexo(Funcs, idcode)
            print(idcode, nomes)
            att2.close()
            Funcs.ShowVendedor(Funcs, homevendedor)
    def UpdateP(self, tabela, carga, processo, protocolo, obs, alertidupdate, att, homeprojetista):
        tabela.currentItem()
        idcode = tabela.currentItem().text()
        if idcode == "":
            alertidupdate.show()
        else:
            cod = ""
            for i in idcode:
                if i.isnumeric() or i == " ":
                    cod += i
            # CARGA
            if carga == "":
                cargas = 7
            else:
                cargaf = ""
                for i in carga:
                    if i.isalnum() or i == " ":
                        cargaf += i
                self.cursor.execute(f"UPDATE db.info SET carga = {cargaf} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET carga = {cargaf} WHERE id = {cod};")
                self.db_connection.commit()
                cargas = 77
            # PROCESSO
            if processo == "":
                processos = 1
            else:
                processof = ""
                for i in processo:
                    if i.isalpha() or i == " ":
                        processof += i
                self.cursor.execute(f"UPDATE db.info SET processo = '{processof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET processo = '{processof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET processo = '{processof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET processo = '{processof}' WHERE id = {cod};")
                self.db_connection.commit()
                processos = 11
            #PROTOCOLO
            if protocolo == "":
                protocolos = 2
            else:
                protocolof = ""
                for i in protocolo:
                    if i.isnumeric() or i == " ":
                        protocolof += i
                self.cursor.execute(f"UPDATE db.info SET protocolo = {protocolof} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET protocolo = {protocolof} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET protocolo = '{protocolof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET protocolo = '{protocolof}' WHERE id = {cod};")
                self.db_connection.commit()
                protocolos = 22
            # CEP
            if obs == "":
                obss = 3
            else:
                obsf = ""
                for i in obs:
                    if i.isalnum() or i == " ":
                        obsf += i
                self.cursor.execute(f"UPDATE db.info SET obs = '{obsf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET obs = '{obsf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET obs = '{obsf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET obs = '{obsf}' WHERE id = {cod};")
                self.db_connection.commit()
                obss = 33

            #Funcs.EnvAnexo(Funcs, idcode)
            att.close()
            Funcs.ShowProjetista(Funcs, homeprojetista)
    def UpdateADM(self, tabela,  nome, cpf, cep, numero, cnc, carga, uc, processo, protocolo, obs, alertidupdate, att3, home):
        tabela.currentItem()
        idcode = tabela.currentItem().text()
        if idcode == "":
            alertidupdate.show()
        else:
            cod = ""
            for i in idcode:
                if i.isnumeric() or i == " ":
                    cod += i
            # NOME
            if nome == None:
                nomes = 1
            else:
                nomef = ""
                for i in nome:
                    if i.isalpha() or i == " ":
                        nomef += i
                self.cursor.execute(f"UPDATE db.info SET cliente = '{nomef}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cliente = '{nomef}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET cliente = '{nomef}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET cliente = '{nomef}' WHERE id = {cod};")
                self.db_connection.commit()
                nomes = 11
            # CPF
            if cpf == "":
                cpfs = 2
            else:
                cpfcnpj = ""
                for i in cpf:
                    if i.isnumeric() or i == " ":
                        cpfcnpj += i
                self.cursor.execute(f"UPDATE db.info SET cpf = {cpfcnpj} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cpf = {cpfcnpj} WHERE id = {cod};")
                self.db_connection.commit()
                cpfs = 22
            # CEP
            if cep == "":
                ceps = 3
            else:
                cepf = ""
                for i in cep:
                    if i.isalnum() or i == " ":
                        cepf += i
                self.cursor.execute(f"UPDATE db.info SET cep = {cepf} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cep = {cepf} WHERE id = {cod};")
                self.db_connection.commit()
                ceps = 33
            # NUMERO
            if numero == "":
                numeros = 4
            else:
                numerof = ""
                for i in numero:
                    if i.isalnum() or i == " ":
                        numerof += i
                self.cursor.execute(f"UPDATE db.info SET numero = {numerof} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET numero = {numerof} WHERE id = {cod};")
                self.db_connection.commit()
                numeros = 44
            # CNC
            if cnc == "":
                cncs = 6
            else:
                cncf = ""
                for i in cnc:
                    if i.isalnum() or i == " ":
                        cncf += i
                self.cursor.execute(f"UPDATE db.info SET cnc = '{cncf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET cnc = '{cncf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET cnc = '{cncf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET cnc = '{cncf}' WHERE id = {cod};")
                self.db_connection.commit()
                cncs = 66
            # CARGA
            if carga == "":
                cargas = 7
            else:
                cargaf = ""
                for i in carga:
                    if i.isalnum() or i == " ":
                        cargaf += i
                self.cursor.execute(f"UPDATE db.info SET carga = {cargaf} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET carga = {cargaf} WHERE id = {cod};")
                self.db_connection.commit()
                cargas = 77
            # UC
            if uc == "":
                ucs = 5
            else:
                ucf = ""
                for i in uc:
                    if i.isnumeric() or i == " ":
                        ucf += i
                self.cursor.execute(f"UPDATE db.info SET uc = {ucf} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET uc = {ucf} WHERE id = {cod};")
                self.db_connection.commit()
                ucs = 55
            if processo == "":
                processos = 1
            else:
                processof = ""
                for i in processo:
                    if i.isalpha() or i == " ":
                        processof += i
                self.cursor.execute(f"UPDATE db.info SET processo = '{processof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET processo = '{processof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET processo = '{processof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET processo = '{processof}' WHERE id = {cod};")
                self.db_connection.commit()
                processos = 11
            #PROTOCOLO
            if protocolo == "":
                protocolos = 2
            else:
                protocolof = ""
                for i in protocolo:
                    if i.isnumeric() or i == " ":
                        protocolof += i
                self.cursor.execute(f"UPDATE db.info SET protocolo = {protocolof} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET protocolo = {protocolof} WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET protocolo = '{protocolof}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET protocolo = '{protocolof}' WHERE id = {cod};")
                self.db_connection.commit()
                protocolos = 22
            # CEP
            if obs == "":
                obss = 3
            else:
                obsf = ""
                for i in obs:
                    if i.isalnum() or i == " ":
                        obsf += i
                self.cursor.execute(f"UPDATE db.info SET obs = '{obsf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.datainfo SET obs = '{obsf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.clientesvendas SET obs = '{obsf}' WHERE id = {cod};")
                self.cursor.execute(f"UPDATE db.projetos SET obs = '{obsf}' WHERE id = {cod};")
                self.db_connection.commit()
                obss = 33
            #Funcs.EnvAnexo(Funcs, idcode)
            att3.close()
            Funcs.ShowADM(Funcs, home)

    #FUNÇÃO DE FILTROS VENDEDOR
    def FiltroDoc(self, homevendedor):
        q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{self.user}' AND processo = 'Documentação';")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homevendedor.tabelavendedor
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroProj(self, homevendedor):
        q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{self.user}' AND processo = 'Criação de Projeto';")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homevendedor.tabelavendedor
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroAna(self, homevendedor):
        q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{self.user}' AND processo = 'Analise'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homevendedor.tabelavendedor
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroVist(self, homevendedor):
        q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{self.user}' AND processo = 'Vistoria'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homevendedor.tabelavendedor
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroTroc(self, homevendedor):
        q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{self.user}' AND processo = 'Troca'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homevendedor.tabelavendedor
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroTroc2(self, homevendedor):
        q = (f"SELECT * FROM db.clientesvendas WHERE vendedor = '{self.user}' AND processo = 'trocado'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homevendedor.tabelavendedor
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    #FUNÇÃO DE FILTROS PROJETISTA
    def FiltroDocP(self, homeprojetista):
        q = (f"SELECT * FROM db.projetos WHERE projetista = '{self.user}' AND processo = 'Documentação';")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homeprojetista.tabelaprojetos
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroProjP(self, homeprojetista):
        q = (f"SELECT * FROM db.projetos WHERE projetista = '{self.user}' AND processo = 'Criação de Projeto';")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homeprojetista.tabelaprojetos
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroAnaP(self, homeprojetista):
        q = (f"SELECT * FROM db.projetos WHERE projetista = '{self.user}' AND processo = 'Analise'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homeprojetista.tabelaprojetos
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroVistP(self, homeprojetista):
        q = (f"SELECT * FROM db.projetos WHERE projetista = '{self.user}' AND processo = 'Vistoria'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homeprojetista.tabelaprojetos
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroTrocP(self, homeprojetista):
        q = (f"SELECT * FROM db.projetos WHERE projetista = '{self.user}' AND processo = 'Troca'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homeprojetista.tabelaprojetos
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroTroc2P(self, homeprojetista):
        q = (f"SELECT * FROM db.projetos WHERE projetista = '{self.user}' AND processo = 'trocado'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = homeprojetista.tabelaprojetos
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    # FUNÇÃO DE FILTRO ADM
    def FiltroDocADM(self, home):
        q = (f"SELECT * FROM db.projetos WHERE processo = 'Documentação';")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = home.table_adm
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroProjADM(self, home):
        q = (f"SELECT * FROM db.projetos WHERE processo = 'Criação de Projeto';")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = home.table_adm
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroAnaADM(self, home):
        q = (f"SELECT * FROM db.projetos WHERE processo = 'Analise'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = home.table_adm
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroVistADM(self, home):
        q = (f"SELECT * FROM db.projetos WHERE processo = 'Vistoria'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = home.table_adm
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroTrocADM(self, home):
        q = (f"SELECT * FROM db.projetos WHERE processo = 'Troca'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = home.table_adm
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def FiltroTroc2ADM(self, home):
        q = (f"SELECT * FROM db.projetos WHERE processo = 'trocado'")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table_projetos = home.table_adm
        table_projetos.setRowCount(len(result))
        table_projetos.setColumnCount(6)
        for i in range(0, len(result)):
            for j in range(0, 6):
                table_projetos.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
    def ClearLine(self, newclient):
        lines = [newclient.line_nome,
                 newclient.line_cpfcnpj,
                 newclient.line_cep,
                 newclient.line_numero,
                 newclient.line_uc,
                 newclient.line_cnc,
                 newclient.line_docs,
                 newclient.line_carga]
        for line in lines:
            line.clear()