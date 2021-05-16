from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import emoji
import time
import random
import credentials


class InstagramBot:
    def __init__(self, username, password):
        self.username = credentials.username
        self.password = credentials.password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"./geckodriver")

        # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/


    #Definindo a url que o bot irá abrir
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        #Fazer login digitando usuário
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)

        #Antes de digitar a senha, ele irá limpar a barra de texto
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()

        #Fazer login digitando a senha
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

        #caso a tela solicitando salvar informações apareça, deixe ativado essa parte, caso contrário, basta comentar o código.
        salvar_suas_informacoes_de_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        salvar_suas_informacoes_de_login.click()
        time.sleep(3)

        #Buscará a hashtag adicionada no credentials.py file
        self.comente_nas_fotos_com_a_hashtag(credentials.hashtag)


    @staticmethod
    #Definindo o robô para escrever como um humano
    def type_like_a_person(sentence, single_input_field):

        #Este código irá basicamente permitir que você simule a digitação como uma pessoa
        print("vou começar a digitar a mensagem na área de texto de compartilhamento de mensagens")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)
    
    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        links_de_posts = []
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        
        #Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser:
        for i in range(1, 3):  #Quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            
        #Faz a contagem das fotos analisadas de acordo com as hashtag
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except:
                pass

        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                #Curte as fotos antes de comentar
                photo_like = driver.find_element_by_class_name('fr66n')
                photo_like.click()
                time.sleep(3)
                
                #Comentários
                comments = [
                    # Remova esses comentários e insira os seus comentários aqui
                    "Wow, amazing! ❤️",
                    "Loved it! ❤️",
                    "Legit! ❤️",
                    "Nice! Keep it up! ❤️",
                    "Should be at top 10 on @instagram, just perfect, I loved it! ❤️",
                ]  
                

                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))

                self.type_like_a_person(
                    random.choice(comments), comment_input_box)
                time.sleep(random.randint(3, 5))

                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(3)

                time.sleep(random.randint(15, 35))
            except Exception as e:
                print(e)
                time.sleep(5)

                


#Puxa as credenciais do arquivo credentials.py
guiBot = InstagramBot(credentials.username, credentials.password)
guiBot.login()
