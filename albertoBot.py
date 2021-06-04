import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import sheetsBot
from selenium.webdriver.common.keys import Keys

"""
Antes de rodar o código:
1. instale as seguintes bibliotecas:
    - Selenium
    - time
    Para instalar a biblioteca basta escreve no promt de comando:
        pip install "biblioteca"
2. Tenha o google chrome e instalado
3. Baixe o chromedriver para utilizar o selenium: 
    https://chromedriver.chromium.org/downloads

"""
class BotAlberto:
    #Não precisa saber disso, mas é tipo um constructor que constroí o bot
    def __init__(self):
        self.driver_path = executable_path="chromedriver.exe" # ATENÇÃO!!! MUDE O DIRETÓRIO CASO NÃO RODE!
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--user-data-dir=/home/username/.config/google-chrome")
        self.chrome =webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
        
        self.jaRespondeu = 0 # 0 = Não - 1 = Sim
        self.mensagemSalva = None
        self.usuarioAtual = None # O usuario para o qual o bot está conectado
        
    """Acessa um site, no caso do Alberto Bot, padroniza-se o whatsapp"""    
    def AcessSite(self):
        #Acessa um site, no caso o site do whatsapp
        self.chrome.get('https://web.whatsapp.com/')

    """Procura um usuario com base no seu nome na barra de pesquisa e acessa caso ache o usuario (Poderia ser um numero também"""
    def ProcuraUsuario(self,usuario):
        self.usuarioAtual = usuario
        sleep(5)
        barraDeTexto = self.chrome.find_elements_by_xpath('//div[contains(@class,"_2_1wd copyable-text selectable-text")]')
        barraDeTexto[0].click()
        barraDeTexto[0].send_keys(f'{usuario}') 
        sleep(2)
        clicarPessoa = self.chrome.find_element_by_xpath(f"//span[@title='{usuario}'][@class='_35k-1 _1adfa _3-8er']") #Procura o nome de uma pessoa
        clicarPessoa.click() # Acessa o contato dessa pessoa
        
    """Envia uma mensagem inicial ao usuário"""
    def MensagemInicial(self,usuario,texto):
           
            #Acessa a barra de texto (região onde vou mandar a mensagem)
            barraDeTexto = self.chrome.find_elements_by_xpath('//div[contains(@class,"_2_1wd copyable-text selectable-text")]')
            barraDeTexto[1].click()
            
            #Manda uma mensagem na barra de texto, dentro da send_keys é basicamente a mensagem que você quer mandar
            barraDeTexto[1].send_keys(texto)
            
            #Procura a setinha de enviar a mensagem e clica nela
            mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
            mandarMensagem.click()
            barraDeTexto[1].click()
            for message in sheetsBot.mensagem:
                barraDeTexto[1].send_keys(message) 
            mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
            mandarMensagem.click()
    """Manda mensagem conforme resposta do usuario"""
    def procuraMensagemEEnviarMensagem(self):
            
            #Dorme por 5 segundos
            sleep(5)
            
            #Procura as mensagens do contato
            try:
                mensagem = self.chrome.find_elements_by_xpath('//div[contains(@class,"GDTQm message-in focusable-list-item")]')

                #Perceba que mensagem é um vetor, pois há várias mensagens, nesse caso vou acessar a última mensagem, o último termo do vetor
                texto = mensagem[len(mensagem)-1] #Lembrando que o vetor começa sempre no zero, então pegamos o total de mensagens e diminuimos de 1.

                #Acessa o conteúdo da mensagem
                procurandoElemento = texto.find_elements_by_class_name("_3-8er")

                conteudoTexto = procurandoElemento[len(procurandoElemento)-1].text
                print(f'{conteudoTexto}')
                #Acessa a barra de texto (região onde vou mandar a mensagem)
                barraDeTexto = self.chrome.find_elements_by_xpath('//div[contains(@class,"_2_1wd copyable-text selectable-text")]')

            except:
                whatsapp.procuraMensagemEEnviarMensagem()
            
            #Responde com base na última resposta do usuário
            if conteudoTexto.lower() in sheetsBot.textinhos and self.jaRespondeu == 0:
                barraDeTexto[1].click()
                barraDeTexto[1].send_keys(f"O(A) Diretor(a) é o(a) {sheetsBot.diretores[sheetsBot.textinhos.index(conteudoTexto.lower())]}")
                mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
                mandarMensagem.click()
                self.jaRespondeu = 1
                self.mensagemSalva = conteudoTexto
                self.enviarMensagem()
                self.enviarFigurinha()
                self.enviaImagem(r"C:\Users\Nauvo\Downloads\mamaco.jpeg")
                whatsapp.procuraMensagemEEnviarMensagem()
                
            elif conteudoTexto.lower() == "continuar" and self.jaRespondeu!=0:
                self.jaRespondeu = 0
                self.mensagemSalva = conteudoTexto
                self.MensagemInicial(self.usuarioAtual,"Digite outra diretoria")
                whatsapp.procuraMensagemEEnviarMensagem()

            elif conteudoTexto.lower() == "nao" or conteudoTexto.lower() == "não" and self.mensagemSalva != conteudoTexto and self.jaRespondeu!=0:
                barraDeTexto[1].click()
                barraDeTexto[1].send_keys(f"Como assim não? ", u'\uF605')
                mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
                mandarMensagem.click()
                self.mensagemSalva = conteudoTexto
                whatsapp.procuraMensagemEEnviarMensagem()

            elif conteudoTexto.lower() == "sim" and self.mensagemSalva != conteudoTexto and self.jaRespondeu!=0:
                barraDeTexto[1].click()
                barraDeTexto[1].send_keys(f"Sim, diretoria!! ", u'\uF494')
                mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
                mandarMensagem.click()
                self.mensagemSalva = conteudoTexto
                whatsapp.procuraMensagemEEnviarMensagem()
                

            elif self.mensagemSalva != conteudoTexto:
                barraDeTexto[1].click()
                barraDeTexto[1].send_keys(f"Não entendi sua resposta, desculpa, ainda estou aprendendo =(")
                mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
                mandarMensagem.click()
                self.mensagemSalva = conteudoTexto
                whatsapp.procuraMensagemEEnviarMensagem()
           
                               
                

              
            
    """Envia uma mensagem padrão para um usuário"""
    def enviarMensagem(self):
        sleep(5)
        barraDeTexto = self.chrome.find_elements_by_xpath('//div[contains(@class,"_2_1wd copyable-text selectable-text")]')
        barraDeTexto[1].click() 
        barraDeTexto[1].send_keys('Obrigado! #BORACASD \n Para novas informações digite "Continuar" ')    
        mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
        mandarMensagem.click()
        #Pegando primeira mensagem da planilha do bot 

        

    "Envia uma imagem ao usuário"
    def enviaImagem(self,caminho_Imagem):
        
        attachment_section = self.chrome.find_element_by_class_name("_2C9f1")
        attachment_section.click()
        image_box = self.chrome.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(caminho_Imagem)
        sleep(3)
        send_button = self.chrome.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()


    def enviarFigurinha(self):
        emoji_section = self.chrome.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[2]/span'
        )
        emoji_section.click()
        sleep(1)
        sticker_section = self.chrome.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[4]/span'
        )
        sticker_section.click()
        sleep(3)
        favoritas_section = self.chrome.find_element_by_xpath(
            '//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div/div[1]/div[1]/div/div/div[2]/span'
        )
        favoritas_section.click()
        sleep(2)
        figurinha = self.chrome.find_element_by_xpath(
            '//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/div[1]/div/span'
        )
        figurinha.click()
        sleep(3)

    """ Encerra o bot"""   
    def FinalizarBot(self):
        self.chrome.quit()

    

#Não precisa se preocupar com esse if kk, basicamente, ele é só pra situações onde há mais de um arquivo de código
if __name__ == '__main__':
    whatsapp = BotAlberto()
    whatsapp.AcessSite()
    sleep(20)
    #Envia mensagens iniciais para esses usuarios
    lista = ["Volvo", "Bastão"] #Cuidado, depende do nome que o usuário está no whatsapp
    for i in lista:
        
        whatsapp.ProcuraUsuario(i)
        whatsapp.MensagemInicial(i,(f'Olá, tudo bem? {i} ',':happy'+"\n"))
        inicio = time.time()
        fim = time.time()
        while fim - inicio < 60:
            whatsapp.procuraMensagemEEnviarMensagem()
            fim = time.time()
            if inicio-fim>10:
                inicio = time.time()
                fim = time.time()
            print(inicio, fim, int(fim-inicio))

    
    
    
     
       




