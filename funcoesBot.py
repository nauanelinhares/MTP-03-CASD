import time
from selenium import webdriver
from time import sleep
import sheetsBot
from selenium.webdriver.common.keys import Keys


class Bot:
    def __init__(self):
        # ATENÇÃO!!! MUDE O DIRETÓRIO CASO NÃO RODE!
        self.driver_path = executable_path = "chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            "--user-data-dir=/home/username/.config/google-chrome")
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

        self.jaRespondeu = 0  # 0 = Não - 1 = Sim
        self.mensagemSalva = None
        self.usuarioAtual = None  # O usuario para o qual o bot está conectado

    """Acessa um site, no caso do Alberto Bot, padroniza-se o whatsapp"""

    def acessarWhatsapp(self):
        # Acessa um site, no caso o site do whatsapp
        self.chrome.get('https://web.whatsapp.com/')

    """Procura mensagens não lidas"""

    def mensagemNaoLida(self):
        try:
            notificacao = self.chrome.find_elements_by_class_name('_38M1B')
            notificacao[0].click()
            return 1
        except:
            return 0

    """Envia uma mensagem inicial ao usuário"""

    def MensagemInicial(self, texto):
        # Acessa a barra de texto (região onde vou mandar a mensagem)
        barraDeTexto = self.chrome.find_elements_by_xpath(
            '//div[contains(@class,"_2_1wd copyable-text selectable-text")]')
        barraDeTexto[1].click()

        # Manda uma mensagem na barra de texto, dentro da send_keys é basicamente a mensagem que você quer mandar
        barraDeTexto[1].send_keys(texto)

        # Procura a setinha de enviar a mensagem e clica nela
        mandarMensagem = self.chrome.find_element_by_xpath(
            "//span[@data-icon='send']")
        mandarMensagem.click()
        barraDeTexto[1].click()
        for message in sheetsBot.mensagem:
            barraDeTexto[1].send_keys(message)
        mandarMensagem = self.chrome.find_element_by_xpath(
            "//span[@data-icon='send']")
        mandarMensagem.click()

    """Direciona o Bot para um grupo de espera"""

    def grupoEspera(self):
        grupos = self.chrome.find_elements_by_xpath(
            "//span[@data-icon='pinned']")
        for grupo in grupos:
            grupo.click()
            sleep(1)

    """Identifica a mensagem do usuário e responde conforme seu conteúdo"""

    def identificarMensagem(self):
        # Dorme por 5 segundos
        sleep(1)
        # Procura as mensagens do contato
        try:
            mensagem = self.chrome.find_elements_by_xpath(
                '//div[contains(@class,"GDTQm message-in focusable-list-item")]')
            # Perceba que mensagem é um vetor, pois há várias mensagens, nesse caso vou acessar a última mensagem, o último termo do vetor
            # Lembrando que o vetor começa sempre no zero, então pegamos o total de mensagens e diminuimos de 1.
            texto = mensagem[len(mensagem)-1]
            # Acessa o conteúdo da mensagem
            procurandoElemento = texto.find_elements_by_class_name("_3-8er")
            conteudoTexto = procurandoElemento[len(procurandoElemento)-1].text
            # Figurinha (Sem dúvidas)
            if conteudoTexto == "9":
                self.enviarFigurinha()
            
            else:

                # Acessa a barra de texto (região onde vou mandar a mensagem)
                barraDeTexto = self.chrome.find_elements_by_xpath('//div[contains(@class,"_2_1wd copyable-text selectable-text")]')
                if conteudoTexto.isdigit():
                    mensagemASerEnviada = sheetsBot.pegarMensagemNumero(int(conteudoTexto))
                    barraDeTexto[1].click()
                    for message in mensagemASerEnviada:
                        barraDeTexto[1].send_keys(message)
                    mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
                    mandarMensagem.click()
                else:
                    print(conteudoTexto)
                    mensagemASerEnviada = sheetsBot.pegarMensagemTexto(conteudoTexto)
                    barraDeTexto[1].click()
                    for message in mensagemASerEnviada:
                        barraDeTexto[1].send_keys(message)
                    mandarMensagem = self.chrome.find_element_by_xpath("//span[@data-icon='send']")
                    mandarMensagem.click()
        except:
            pass

    "Envia uma imagem ao usuário"

    def enviaImagem(self, caminho_Imagem):

        attachment_section = self.chrome.find_element_by_class_name("_2C9f1")
        attachment_section.click()
        image_box = self.chrome.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(caminho_Imagem)
        sleep(3)
        send_button = self.chrome.find_element_by_xpath(
            '//span[@data-icon="send"]')
        send_button.click()

    "Envia uma figurinha ao usuário"

    # Adicionar http://sticker.ly/s/DWIY60 no Whatsapp Business
    def enviarFigurinha(self):
        emoji_section = self.chrome.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[2]/span'
        )
        emoji_section.click()
        sleep(0.5)
        sticker_section = self.chrome.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[4]/span'
        )
        sticker_section.click()
        sleep(1)
        albertin_section = self.chrome.find_elements_by_xpath(
            '//div[contains(@class,"YAIhH _1eeWL")]'
        )
        albertin_section[2].click()
        sleep(3)
        figurinha = self.chrome.find_element_by_xpath(
            '//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/div[1]/div/span'
        )
        figurinha.click()

    """ Encerra o bot"""

    def FinalizarBot(self):
        self.chrome.quit()
