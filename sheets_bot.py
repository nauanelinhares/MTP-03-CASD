import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("casd-bot-1593e787a9bc.json", scope)
client = gspread.authorize(creds)

sheet = client.open("CASDBotTree").worksheet("TreeNoEmoji")

# Armazenar data da tabela
nros   = sheet.col_values(1)
emojis = sheet.col_values(2)
textos = sheet.col_values(3)
opcoes = sheet.get('D:M')

# Encontrar tamanhos pra evitar panes futuras
size_nros   = len(nros)
size_opcoes = len(opcoes)

# Primeira mensagem
linha_nro = 3

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

