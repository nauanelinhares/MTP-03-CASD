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
        
        "Botoes"

        #Iniciar
        self.botaoIniciar = QPushButton("Iniciar")
        self.layout.addWidget(self.botaoIniciar)
        self.botaoIniciar.clicked.connect(self.botaoIniciarAlberto)

        #EnviarMensagemInicial
        self.botaoMensagemInicial = QPushButton("Iniciar Mensagem")
        self.layout.addWidget(self.botaoMensagemInicial)
        self.botaoMensagemInicial.clicked.connect(self.enviarMensagemInicial)
        
        ### Finalizar o Bot
        self.botaoFim = QPushButton("Finalizar")
        self.layout.addWidget(self.botaoFim)
        self.botaoFim.clicked.connect(self.fecharAlberto)
        
        self.texto.setAlignment(Qt.Alignment.AlignHCenter | Qt.Alignment.AlignTop)
        #Abrir Interface
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
        lista = ["Nauane Linhares", "Bastão"] #Cuidado, depende do nome que o usuário está no whatsapp
        for i in lista:
            self.albertoBot.jaRespondeu = 0
            self.albertoBot.ProcuraUsuario(i)

            self.albertoBot.MensagemInicial(i,(f'Olá, tudo bem? {i} ',':happy'+"\n"))
            self.albertoBot.procuraMensagemEEnviarMensagem()
            

        """
        self.widget = QComboBox()
        self.layout.addWidget(self.widget)
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
        self.layout.addWidget(self.texto)
        self.layout.addWidget(self.imagem)
        font = self.interface.font()
        font.setPointSize(14)
        self.interface.setFont(font)
        self.texto.setAlignment(Qt.Alignment.AlignHCenter | Qt.Alignment.AlignTop)
        self.imagem.setAlignment(Qt.Alignment.AlignHCenter)
        self.setCentralWidget(self.interface)

        
        self.interface = QWidget()
        self.layout = QlayoutLayout(self.interface)
        self.botao = QPushButton('Mandar mensagens para várias pessoas')
        self.layout.addWidget(self.botao, 0, 0, 0 , 1)
        self.botao1 = QPushButton('Mandar Arquivo')
        self.layout.addWidget(self.botao1,0 , 1, 0 , 1)
        self.botao.clicked.connect(lambda: print('Olá Mundo'))
        self.setCentralWidget(self.interface)
        
        self.interface = QWidget()
        self.layout = QlayoutLayout(self.interface)

        
        #Botoes
        self.mandarMensagem = QPushButton("Mandar Mensagem")
        
        
        #Signals - Meio que mostram mensagens na tela
        self.mandarMensagem.setCheckable(True)
        self.mandarMensagem.clicked.connect(self.botaofoiclicado)
        self.mandarMensagem.clicked.connect(self.verSeObotaoFoiClicado)
        self.enviarPdf = QPushButton("Enviar pdf")       
        self.layout.addWidget(self.mandarMensagem, 0, 0, 0 , 1)
        self.layout.addWidget(self.enviarPdf, 0, 1, 0 , 1)
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
    programaIniciar.setStyle("Fusion")
    programa = programaAlberto()
    programa.show()
    programaIniciar.exec()


