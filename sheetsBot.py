import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.keys import Keys
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("casd-bot-1593e787a9bc.json", scope)
client = gspread.authorize(creds)

sheet = client.open("CASDBotTree").worksheet("TreeAlberto")
df = pd.DataFrame(sheet.get_all_records(head = 3))



def pegarMensagem(i):
    
    df.set_index("Nros.", inplace = True)
    numero = i
    texto = pd.DataFrame(df.loc[[numero], 'Textos']).iloc[0,0]
    textos = texto.split("\n")
    mensagem = [x +Keys.SHIFT + Keys.ENTER for x in textos]
    return mensagem
def mensagemErro():
    df.set_index("Nros.", inplace = True)
    numero = 0
    texto = pd.DataFrame(df.loc[[numero], 'Textos']).iloc[0,0]
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