'''
Teste Web Insights
Você é responsável por desenvolver um robô de captação (Crawler) em Python (com
simulação de navegador - selenium).
O robô deve receber um parâmetro “region” e pegar todos os nomes (name), símbolos
(symbol) e preços (price (intraday)) do site https://finance.yahoo.com/screener/new.
Por fim, deve salvar o resultado em um arquivo csv
'''
from selenium import webdriver
from time import sleep # Apagar?

class Robo():
    
    def __init__(self, caminho_driver):
        '''
        Ao instanciar a classe o constructor cria um robô utilizando o navegador Chrome, e acessa a url
        passada como parâmetro, utilizando o driver especificado no caminho_driver (diretório)
        '''
        # É necessário possuir o driver 'chromedriver' que suporte a versão do navegador a ser utilizado
        # no mesmo diretório do script
        self.navegador = webdriver.Chrome()#caminho_driver)
    
    def pegar_dados(self, url):
        try:
            self.navegador.implicitly_wait(15)
            self.navegador.get(url)
            
            # self.titulo = self.navegador.title
            # elemento = self.navegador.find_element_by_tag_name('name')
            self.navegador.find_element_by_xpath('//*[@id="yfin-usr-qry"]').click()
            # self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[5]/div/div[1]/svg').click()
            # self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button/svg/path').click()
            # self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[2]/div/div/svg').click()
            # self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]').click()

        except:
            self.driver.close()
            print('Erro fatal!')

    def desligar_robo(self):
        self.navegador.close()

print('..'*20,'começando')
robo = Robo('')#C:\\datascience\\chromedriver.exe')
robo.pegar_dados('https://finance.yahoo.com/screener/new')
# controle = input('Deseja sair?')
# if controle == 's':
#     robo.desligar_robo()