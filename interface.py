import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import albertoBot

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class Interface (QMainWindow):
    def __init__ (self):
        super().__init__()
        #Tamanho da Interface
        
        #Titulo da Interface
        self.setWindowTitle("Alberto Bot")
        #Nossa interface
        self.interface = QWidget()
        #Mensagem
        self.texto = QLabel("Olá, este é o Alberto Bot, selecione o que você quer fazer!")
        
        #Fonte do texto
        font = self.texto.font()
        font.setPointSize(14)
        self.texto.setFont(font)
        #Imagem
        
        self.grid = QVBoxLayout(self.interface)
        #Botoes
        self.iniciar = QPushButton("Iniciar")
        self.fim = QPushButton("Finalizar")
        self.grid.addWidget(self.texto)
    

        self.grid.addWidget(self.iniciar)
        self.iniciar.clicked.connect(self.iniciarAlberto)
        self.grid.addWidget(self.fim)
        self.fim.clicked.connect(self.fecharAlberto)
        
        self.texto.setAlignment(Qt.Alignment.AlignHCenter | Qt.Alignment.AlignTop)
        self.setCentralWidget(self.interface)


    def iniciarAlberto(self):
        self.hide()
        albertoBot.iniciar()
        self.show()

    def fecharAlberto(self):
        self.fim.setDisabled(True)
        self.close()        
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
    programaAlberto = QApplication(sys.argv)
    interfaceAlberto = Interface()
    interfaceAlberto.show()
    programaAlberto.exec()


