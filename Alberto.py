import sys
from time import sleep
import time
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import funcoesBot

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
        
        "Alberto"
        self.albertoBot = None

        "Interface do Albertinho"
        #Tamanho da Interface
        
        #Titulo da Interface
        self.setWindowTitle("Alberto Bot")
        #Nossa interface
        self.interface = QWidget()
        self.grid = QVBoxLayout(self.interface)
        #Mensagem
        self.texto = QLabel("Olá, este é o Alberto Bot, selecione o que você quer fazer!")
        self.grid.addWidget(self.texto)
        #Fonte do texto
        font = self.texto.font()
        font.setPointSize(14)
        self.texto.setFont(font)
        #Imagem
        #Botoes
        self.botaoIniciar = QPushButton("Iniciar")
        self.grid.addWidget(self.botaoIniciar)
        self.botaoIniciar.clicked.connect(self.botaoIniciarAlberto)

        self.botaoMensagemInicial = QPushButton("Iniciar Mensagem")
        self.grid.addWidget(self.botaoMensagemInicial)
        self.botaoMensagemInicial.clicked.connect(self.enviarMensagemInicial)
        
        ### Finalizar o Bot
        self.botaoFim = QPushButton("Finalizar")
        self.grid.addWidget(self.botaoFim)
        self.botaoFim.clicked.connect(self.fecharAlberto)
        
       # self.texto.setAlignment(Qt.Alignment.AlignHCenter | Qt.Alignment.AlignTop)
        self.setCentralWidget(self.interface)


    def botaoIniciarAlberto(self):
        self.botaoIniciar.setDisabled(True)
        self.albertoBot = funcoesBot.Bot()
        self.albertoBot.acessarWhatsapp()
        sleep(10)

    def fecharAlberto(self):
        self.botaoFim.setDisabled(True)
        self.albertoBot.FinalizarBot() 
        self.close()     
          
    def enviarMensagemInicial(self):
         #Envia mensagens iniciais para esses usuarios

        while True:
            self.albertoBot.mensagemNaoLida()
            
     #   inicio = time.time()
     #   fim = time.time()
     #   while fim - inicio < 60:
     #       tempoAntesDeExecutar = time.time()
     #       self.albertoBot.procuraMensagemEEnviarMensagem()
     #       fim = time.time()
     #       print(fim - inicio)
     #       if fim - tempoAntesDeExecutar>10:
     #           inicio = time.time()
     #           fim = time.time()

        """
        self.widget = QComboBox()
        self.grid.addWidget(self.widget)
        self.widget.addItems(["Bastão", "Manga", "Volvo", "Joseph"])
        self.widget.currentIndexChanged.connect( self.index_changed)
        # There is an alternate signal to send the text.
        self.widget.currentTextChanged.connect(self.text_changed)
        self.widget.setEditable(True)
        self.setCentralWidget(self.interface)
    def index_changed(self,i):
            print(i)
    def text_changed(self,s):
            print(s)


    
       
        self.texto = QLabel("Olá, este é o Alberto Bot, marque o que você quer fazer!")
        self.imagem = QLabel("Olá, este é o Alberto Bot, escreva o que você quer fazer!")
        
        self.texto.setScaledContents(True)
        self.grid.addWidget(self.texto)
        self.grid.addWidget(self.imagem)
        font = self.interface.font()
        font.setPointSize(14)
        self.interface.setFont(font)
        self.texto.setAlignment(Qt.Alignment.AlignHCenter | Qt.Alignment.AlignTop)
        self.imagem.setAlignment(Qt.Alignment.AlignHCenter)
        self.setCentralWidget(self.interface)

        
        self.interface = QWidget()
        self.grid = QGridLayout(self.interface)
        self.botao = QPushButton('Mandar mensagens para várias pessoas')
        self.grid.addWidget(self.botao, 0, 0, 0 , 1)
        self.botao1 = QPushButton('Mandar Arquivo')
        self.grid.addWidget(self.botao1,0 , 1, 0 , 1)
        self.botao.clicked.connect(lambda: print('Olá Mundo'))
        self.setCentralWidget(self.interface)
        
        self.interface = QWidget()
        self.grid = QGridLayout(self.interface)

        
        #Botoes
        self.mandarMensagem = QPushButton("Mandar Mensagem")
        
        
        #Signals - Meio que mostram mensagens na tela
        self.mandarMensagem.setCheckable(True)
        self.mandarMensagem.clicked.connect(self.botaofoiclicado)
        self.mandarMensagem.clicked.connect(self.verSeObotaoFoiClicado)
        self.enviarPdf = QPushButton("Enviar pdf")       
        self.grid.addWidget(self.mandarMensagem, 0, 0, 0 , 1)
        self.grid.addWidget(self.enviarPdf, 0, 1, 0 , 1)
        self.setCentralWidget(self.interface)

        def botaofoiclicado(self):
        self.mandarMensagem.setText("Carregando...")
        self.mandarMensagem.setEnabled(False)
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central texto of the Window.
        self.setCentralWidget(container)
        def verSeObotaoFoiClicado(self, checked):
        print("Você clicou?",checked)    
    """
        
        
if __name__ == '__main__':
    programaIniciar = QApplication(sys.argv)
    programa = programaAlberto()
    programa.show()    
    programaIniciar.exec()
    


