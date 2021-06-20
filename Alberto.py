import sys
from time import sleep
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
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
        uic.loadUi('AlbertoUI.ui', self)

        
        "Processos"
        
        
        "Alberto"
        self.albertoBot = None

        "Interface do Albertinho"
        #Tamanho da Interface
        
        "Titulo da Interface"
        self.setWindowTitle("Alberto Bot")
        self.setWindowIcon(QIcon('alberto.ico'))

        "Bot"
        self.albertoBot = funcoesBot.Bot()            
        "Botoes"
        #Iniciar
        
        self.botaoIniciar.clicked.connect(self.ProcessoIniciar)

        #EnviarMensagemInicial
        self.processoAtivarMensagem = None
        self.botaoMensagemInicial.setCheckable(True)
        self.botaoMensagemInicial.clicked.connect(self.ProcessoAtivarMensagem)
        self.booleana = 0
        ### Finalizar o Bot
        
        self.botaoFim.clicked.connect(self.ProcessoFinalizarBot)
        self.botao = QPushButton("Iniciar") 
    
        #onoff
        
        


        
        
    def ProcessoIniciar (self):
        #Inicia
        self.processoIniciar = threading.Thread(target = self.botaoIniciarAlberto)
        self.processoIniciar.start()

    def ProcessoAtivarMensagem (self,checked):
        if checked:
            self.processoAtivarMensagem = threading.Thread(target= self.enviarMensagemInicial)
            self.booleana = 1
            self.processoAtivarMensagem.start()
            self.onoff.setChecked(True)
   
        else:
          
            self.booleana = 0
            self.processoAtivarMensagem.join()
            self.onoff.setChecked(False)
   

            

    def ProcessoFinalizarBot (self):
        self.processoFinalizarBot = threading.Thread(target= self.fecharAlberto)
        self.processoFinalizarBot.start()   



    def botaoIniciarAlberto(self):
        self.botaoIniciar.setDisabled(True)
        self.botaoIniciar.setStyleSheet(
                    """QPushButton {
                    color: #333;
                    border: 2px solid #555;
                    border-radius: 20px;
                    border-style: outset;
                    background: qradialgradient(
                        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
                        radius: 1.35, stop: 0 #fff, stop: 1 #888
                        );
                    padding: 5px;
                    font: 20pt "Lobster 1.4";
                    color: rgb(255,255,255);
                    background-color: rgb(194, 194, 194);
                    
                    }
                    }""")
        self.albertoBot.acessarWhatsapp()
        sleep(10)

    def fecharAlberto(self):
        self.botaoFim.setDisabled(True)
        self.albertoBot.FinalizarBot() 
        self.close()     
          
    def enviarMensagemInicial(self):
        # Envia mensagens iniciais para esses usuarios
        while self.booleana:
            boolean = self.albertoBot.mensagemNaoLida()
            sleep(1)
            if boolean == 1:
                self.albertoBot.identificarMensagem()
                sleep(1)
            self.albertoBot.grupoEspera()
            sleep(1)
    
            
        
        
if __name__ == '__main__':
    programaIniciar = QApplication(sys.argv)
    programaIniciar.setStyle("Fusion")
    programa = programaAlberto()
    programa.show()
    programaIniciar.exec()
    


