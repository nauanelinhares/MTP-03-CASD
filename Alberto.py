import sys
from time import sleep
import time
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import funcoesBot
import os
import threading
"""
Antes de rodar o código:
1. instale as seguintes bibliotecas:
    - Selenium
    - time
    - PyQt6
    - PyQt5
    - gspread
    Para instalar a biblioteca basta escreve no promt de comando:
        pip install "biblioteca"
2. Tenha o google chrome e instalado
3. Baixe o chromedriver para utilizar o selenium: 
    https://chromedriver.chromium.org/downloads

"""



class programaAlberto (QMainWindow):
    def __init__ (self):
        super().__init__()
        
        "Processos"
        
        
        "Alberto"
        self.albertoBot = None

        "Interface do Albertinho"
        #Tamanho da Interface
        
        "Titulo da Interface"
        self.setWindowTitle("Alberto Bot")
        "Nossa interface"
        self.interface = QWidget()
        self.layout = QVBoxLayout(self.interface)
        #Mensagem
        self.texto = QLabel("Olá, eu sou Alberto Bot, selecione o que você quer fazer!")
        self.layout.addWidget(self.texto)
        #Fonte do texto
        font = self.texto.font()
        font.setPointSize(14)
        self.texto.setFont(font)
        #Imagem
        self.imagem = QLabel()
        self.imagem.setPixmap(QPixmap("alberto.jpg"))
        self.imagem.setFixedSize(QSize(320,240))
        self.imagem.setScaledContents(True)
        self.imagem.setAlignment(Qt.Alignment.AlignCenter)
        self.layout.addWidget(self.imagem)
        
        
        "Bot"
        self.albertoBot = funcoesBot.Bot()            
        "Botoes"
        #Iniciar
        self.processo1 = threading.Thread(target = self.botaoIniciarAlberto)
        self.botaoIniciar = QPushButton("Iniciar")
        self.layout.addWidget(self.botaoIniciar)
        self.botaoIniciar.clicked.connect(self.Processo1)

        #EnviarMensagemInicial
        self.processo2 = threading.Thread(target= self.enviarMensagemInicial)
        self.botaoMensagemInicial = QPushButton("Iniciar Mensagem")
        self.layout.addWidget(self.botaoMensagemInicial)
        self.botaoMensagemInicial.clicked.connect(self.Processo2)
        
        ### Finalizar o Bot
        self.processo3 = threading.Thread(target= self.fecharAlberto)
        self.botaoFim = QPushButton("Finalizar")
        self.layout.addWidget(self.botaoFim)
        self.botaoFim.clicked.connect(self.Processo3)
        
        #Abrir Interface
        self.setCentralWidget(self.interface)
        
        
    def Processo1 (self):
        self.processo1.start()
    def Processo2 (self):
        self.processo2.start()
    def Processo3 (self):
        self.processo3.start()        

    def botaoIniciarAlberto(self):
        self.botaoIniciar.setDisabled(True)
        
        self.albertoBot.acessarWhatsapp()
        sleep(10)

    def fecharAlberto(self):
        self.botaoFim.setDisabled(True)
        print('k')
        self.albertoBot.FinalizarBot() 
        self.close()     
          
    def enviarMensagemInicial(self):
         #Envia mensagens iniciais para esses usuarios
        while True:
            self.albertoBot.mensagemNaoLida()

            self.albertoBot.identificarMensagem()

            self.albertoBot.grupoEspera()

            sleep(3)
            
        
        
if __name__ == '__main__':
    programaIniciar = QApplication(sys.argv)
    programaIniciar.setStyle("Fusion")
    programa = programaAlberto()
    programa.show()    
    programaIniciar.exec()
    


