import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.keys import Keys
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("casd-bot-1593e787a9bc.json", scope)
client = gspread.authorize(creds)

sheet = client.open("CASDBotTree").worksheet("TreeAlberto")

df = pd.DataFrame(sheet.get_all_records(head = 3))
df.set_index("Nros.", inplace = True)

def pegarMensagemNumero(i):
    print('numero',i)
    numero = i
    
    try:
        texto = pd.DataFrame(df.loc[[numero], 'Mensagens']).iloc[0,0]
        print("kkkkkkkkkkkkkkkkkk")
    except:
        texto = sheet.acell("C2").value
    #print(texto)
    textos = texto.split("\n")
    mensagem = [x +Keys.SHIFT + Keys.ENTER for x in textos]
    print("fim")
    return mensagem
def pegarMensagemTexto(mensagem):
    
    try:
        texto = pd.DataFrame(df.loc[[mensagem], 'Mensagens']).iloc[0,0]
    except:
        texto = sheet.acell("C2").value
    textos = texto.split("\n")
    mensagem = [x +Keys.SHIFT + Keys.ENTER for x in textos]
    return mensagem






