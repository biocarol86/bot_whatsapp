from selenium import webdriver
import time  # biblioteca para dá um tempo


class WhatsappBot:
    def __init__(self):  # Dá um comportamento inicial ao programa
        self.mensagem = "Bom dia!Bom domingo!"  # A mensagem q irá enviar ao grupo
        self.grupos = "Amigos"  # Nome do grupo que vc irá mandar mensagens, tem que ser igual como está escrito
        options = selenium.webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')  # Usar a linguagem em português
        self.driver = selenium.webdriver.Chrome(executable_path=r'C:\Users\Maria Carolina\Desktop\Bot whatsapp\chromedriver.exe')

    def EnviarMensagem(self):
        # <span dir="auto" title="Café com os amigos" class="_35k-1 _1adfa _3-8er">Café com os amigos</span>
        # <div tabindex="-1" class="_2A8P4">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title= '{grupo}']")
            time.sleep(3)  # Dá um tempo de 3 segundos na execução do programa para não travar
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_2A8P4')  # Encontrar a referencia da caixa de texto
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)  # Enviar mensagem para o grupo
            botao = self.driver.find_element_by_xpath("//span[@data-icon='send']")  # As aspas precisam ser diferentes
            time.sleep(3)
            botao.click()


bot = WhatsappBot()
bot.EnviarMensagem()
