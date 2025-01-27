from imap_tools import MailBox, AND
import re
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from teste import functions

user = "easybot@northtc.com.br"
pasw = "MinibotNTC@4761"

meu_email = MailBox("imap.hostinger.com").login(user, pasw)

lista_emails = meu_email.fetch(AND(from_="comercial@northtc.com.br"))
for email in lista_emails:
    eml = email.text
    start = '</b><br />'
    end = '</li>'
    result = re.split(r'<br />|</li>', eml)
    test = 0
    '''for info in result:
        print("---------------------------------")
        print(info)
        print(test)
        test += 1'''
    
    tp_pessoa = result[1]
    #Procuração
    nome = result[3]
    uc = result[7]
    cnc = result[9]
    rg = result[5]
    cpf = result[11]
    ruaf = result[13].split('</strong> ')
    rua = ruaf[1]
    numero = result[18]
    bairro = result[20]
    cidadef = result[14].split('</strong> ')
    cidade = cidadef[1]
    estadof = result[15].split('</strong> ')
    estado = estadof[1]
    cepf = result[16].split('</strong> ')
    cep = cepf[1]

    #DadosAneel
    classe = result[22]
    qtdmod = result[24]
    fabmod = result[26]
    modmod = result[28]
    qtdinversor = result[30]
    fabinversor = result[32]
    modinversor = result[34]
    somamod = result[36]
    somainversor = result[38]
    areaarranjo = result[40]
    dataprev = result[42]

    #Formulario
    lttd = result[45]
    lgtd = result[47]
    cargainsta = result[49]
    cargainstagera = result[51]
    tensao = result[53]

    kit = result[55]
    fase = result[57]
    disjuntor = result[59]
    pot_nom_mod = result[61]
    qtd_arranjo = result[63]
    serie_arranjo = result[65]
    pot_nom_inv = result[67]
    qtd_entrada_inv = result[69]
    espe_cc = result[71]
    espe_ca = result[73]

    if tp_pessoa == 'Física':
        print("1")
        #functions.ProcuracaoPF(nome, cpf, rg, rua, numero, bairro, cidade, estado, cep, cnc, uc)
        #functions.DadosAneel(nome, cpf, rua, numero, bairro, cidade, cep, uc, classe, disjuntor, qtdmod, fabmod, modmod, areaarranjo, qtdinversor, fabinversor, modinversor, somamod, somainversor, dataprev)
        functions.Formulario10KW(nome, cpf, rua, numero, bairro, cidade, cep, uc, classe, lttd, lgtd, cargainsta, cargainstagera, tensao)
    elif tp_pessoa == 'Jurídica':
        #functions.ProcuracaoPJ(nome, cpf, rg, rua, numero, bairro, cidade, estado, cep, cnc, uc)
        #functions.DadosAneel(nome, cnpj, rua, numero, bairro, cidade, cep, uc, classe, disjuntor, qtdmod, fabmod, modmod, areaarranjo, qtdinversor, fabinversor, modinversor, somamod, somainversor, dataprev)
        print("2")
