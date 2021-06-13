import string
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.keys import Keys
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("casd-bot-1593e787a9bc.json", scope)
client = gspread.authorize(creds)

sheet = client.open("CASDBotTree").worksheet("TreeAlberto")

def pegarMensagem(i):
    num = int(i)+4
    celula = "N"+str(num)
    texto = sheet.acell(celula).value
    textos = texto.split("\n")
    mensagem = [x +Keys.SHIFT + Keys.ENTER for x in textos]
    print(mensagem)
    return mensagem
def mensagemErro():
    texto = sheet.acell("N2").value
    textos = texto.split("\n")
    mensagem = [x +Keys.SHIFT + Keys.ENTER for x in textos]
    return mensagem
# Armazenar data da tabela
"""
nros   = sheet.col_values(1)
emojis = sheet.col_values()
textos = sheet.col_values(3)[3:]
diretores = sheet.col_values(4)[3:]
"""

x = pegarMensagem(0)
# Encontrar tamanhos pra evitar panes futuras

# Funcao que pega a mensagem




"""
textinhos = [x.lower() for x in textos]


while True:
    # Texto prinicipal da mensagem
    mensagem = '\n' + textos[linha_nro] 
    
    # Se tiver opcoes, concatena
    if linha_nro + 1 <= size_opcoes:
        qtd_opcoes = len(opcoes[linha_nro])
        for i in range(qtd_opcoes):
            mensagem += '\n' + opcoes[linha_nro][i]
            i += 1
        
    
    # Se nao for o menu, concatena como acessá-lo
    if linha_nro != 3:
        mensagem += '\n\n' + textos[0]
    
    # Dispor mensagem e pegar próximo numero
    mensagem += '\n\nNumero: '
    nro = input(mensagem)
    print("\n.\n.\n.\n")

    # Encontrar linha do numero escolhido
    linha_nro = 1
    for i in range(size_nros):
        if nro == nros[i]:
            linha_nro = i

"""