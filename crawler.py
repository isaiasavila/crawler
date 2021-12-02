'''
Teste Web Insights
Você é responsável por desenvolver um robô de captação (Crawler) em Python (com
simulação de navegador - selenium).
O robô deve receber um parâmetro “region” e pegar todos os nomes (name), símbolos
(symbol) e preços (price (intraday)) do site https://finance.yahoo.com/screener/new.
Por fim, deve salvar o resultado em um arquivo csv
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

class Robo():
    
    def __init__(self, caminho_driver):
        '''
        Ao instanciar a classe o constructor cria um robô utilizando o navegador Chrome, e acessa a url
        passada como parâmetro, utilizando o driver especificado no caminho_driver (diretório)
        '''
        # É necessário possuir o driver 'chromedriver' que suporte a versão do navegador a ser utilizado
        # no mesmo diretório do script
        self.options = Options()
        self.options.add_argument('window-size=800,600')
        # self.options.add_argument('window-size=1366,768')
        # Oculta o navegador
        # self.options.add_argument('--headless')
        self.navegador = webdriver.Chrome(caminho_driver,options=self.options)
    
    def pegar_dados(self, url):
        try:
            # 
            self.navegador.get(url)
            # 
            sleep(10)
            # self.navegador.find_element_by_xpath('//*[@id="yfin-usr-qry"]').send_keys('Lulu Chiang').submit()
            # self.navegador.find_element_by_xpath('//*[@id="header-desktop-search-button"]').click()
            # Limpa a seleção do país padrão (USA)
            self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button').click()
            # Habilita a seleção dos países desejados
            self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul').click()
            # paises = ('Argentina', 'Austria', Australia', 'Belgium', 'Brazil', 'Canada', 'Switzerland', 'Chile', 'China', 'Czech Republic', 'Germany', 'Denmark', 'Estonia', 'Egypt', 'Spain', 'Finland', 'France', 'United Kingdom', 'Greece', 'Hong Kong', 'Hungary', 'Indonesia', 'Ireland', 'Israel, 'India', 'Iceland', 'Japan', 'South Korea', 'Kuwait', 'Sri Lanka', 'Lithuania', 'Latvia', 'Mexico', 'Malaysia', 'Netherlands', 'Norway', 'New Zealand', 'Peru', 'Philippines', 'Pakistan', 'Poland', 'Portugal', 'Qatar','Russia', 'Saudi Arabia', 'Sweden', 'Singapore', 'Suriname', 'Thailand', 'Turkey', 'Taiwan', 'United States', 'Venezuela', 'Vietnam', 'South Africa')
            # paises = ('Austria','Argentina','Australia')
            # Tupla contendo os check-boxes dos países que serão selecionados
            checks = ('//*[@id="dropdown-menu"]/div/div[2]/ul/li[2]/label/input','//*[@id="dropdown-menu"]/div/div[2]/ul/li/label/input','//*[@id="dropdown-menu"]/div/div[2]/ul/li[3]/label/input')
            # Laço de repetição para a seleção dos países desejados (region)
            # Controlador para utilização da tupla
            controle = True
            if controle == 'True':
                for cont in range(len(checks)):
                    # Tupla servindo como parâmetro de seleção
                    self.navegador.find_element_by_xpath(checks[cont]).click()
            else:
                # Linha de teste
                self.navegador.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[2]/label/input').click()
            # Parada para página ser devidamente atualizada
            # sleep(10)
            # Mapeia o botão de resultados
            elemento = self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]')
            sleep(10)
            # Clique no botão de resultados
            elemento.click()
            # self.navegador.implicitly_wait(25)
            # elemento.click()
            sleep(10)
            conteudo = self.navegador.page_source
            site = BeautifulSoup(conteudo,'html.parser')
            # Impressão do código fonte da página
            # print(site.prettify())
            
            #TESTE
            bsObj = BeautifulSoup(conteudo,'html.parser')
            #print(bsObj)
            dados_tabela = bsObj.find('div',{'id':'fin-scr-res-table'})
            get_corpo_tabela = dados_tabela.tbody
            print('|'*25)
            # print(dados_tabela)
            # print(get_corpo_tabela)
            linhas = get_corpo_tabela.find_all('tr')
            i = 0
            dados = {}
            
            for linha in linhas:
                colunas = linha.find_all('td')
                simbolo = colunas[0].get_text()
                nome = colunas[1].get_text()
                preco = colunas[2].get_text()
                dados[i]= str(simbolo +','+ nome +','+ preco)
                i += 1
                # print(simbolo,nome,preco,sep='<|>')
            # print(f'Registros: {i}')
            # print(dados)
            # dados_tabela = site.find('div',{'id':'screener-results'})
            # print(dados_tabela.prettify())
            # nome = site.find('div', attrs={})
            # simbolo = site.find('div', attrs={})
            # preco = site.find('div', attrs={})
            
        except:
            self.desligar_robo()
            print('Erro!')

    def desligar_robo(self):
        self.navegador.close()

print('..'*20,'começando')
robo = Robo('C:\\datascience\\chromedriver.exe')
robo.pegar_dados('https://finance.yahoo.com/screener/new')
# controle = input('Deseja sair?')
# if controle == 's':
#     robo.desligar_robo()
# self.titulo = self.navegador.title
# E2 = self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]/span')
# E2.click()
# Clique do botão de mostrar resultados
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]').click()
# elemento = self.navegador.find_element_by_tag_name('name')
# self.navegador.find_element_by_xpath('//*[@id="yfin-usr-qry"]').click()
# svg
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div').click()
# div
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li/div/div').click()
# element = self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]')
# element.send_keys("", Keys.ESC)
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]').send_keys(Keys.ESC)
# Desmarca as opções que não serão utilizadas
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul').click()
# self.navegador.find_element_by_xpath('//*[@id="dropdown-menu"]/button/svg').click()
# self.navegador.implicitly_wait(15)
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[5]/div/div[1]/svg').click()
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]/button/svg/path').click()
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[2]/div/div/svg').click()
# self.navegador.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]').click()