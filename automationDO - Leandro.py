from selenium import webdriver
import time

#FUNÇÃO BUSCAR LINKS
def get_all_links(driver):
    links = []
    element = driver.find_element_by_id('dgDocumentos')
    elements = element.find_elements_by_tag_name('a')
    for elem in elements:
        href = elem.get_attribute("href")
        links.append(elem.text)
        links.append(href)
        #print(elem.text)
    return links




#ABRE NAVEGADOR CHROME
web = webdriver.Chrome()
web.get('http://diariooficial.rn.gov.br/dei/dorn3/Search.aspx')
time.sleep(2)

#PESQUISA PALAVRA CHAVE
PalavraChave = "Extrato"
Pchave = web.find_element_by_xpath('//*[@id="input-bs-keyword"]')
Pchave.send_keys(PalavraChave)

#CLICA BOTÃO
Submit = web.find_element_by_xpath('//*[@id="submit-busca-simples"]')
Submit.click()
time.sleep(60)
#//*[@id="Form1"]/section[2]/div/div[2]/a[2]
#t = web.find_element_by_xpath('//*[@id="dgDocumentos"]/tbody/tr[2]/td[1]/a')
#t.click() 

links = []
linkcerto = []
i = 0;
while True:
    links = get_all_links(web);
    for link in links :
        if link is not None:
            #if 'docview' in link:
                linkcerto.append(link)
                 #print(link)
    t = web.find_element_by_xpath('//*[@id="Form1"]/section[2]/div/div[2]/a[2]')
    t.click()
    i = i + 1
    #time.sleep(10)
    if(i == 5):
        #time.sleep(30)
        #i = i + 1
        break
        
    
print(linkcerto)
print('link certo posição 1: ' , linkcerto[0])

for link in linkcerto:
    web.get(link)
    time.sleep(5)
    

    
# falta (1): abrir proximas páginas e guardar os links certos
# falta (2): selecionar informações apenas de links corretos 
# falta (3): pegar as informações  


# (1) - opção 1 : pelo tempo interromper que abra a página repetida 
# https://stackoverflow.com/questions/53955988/how-to-move-to-the-next-page-on-python-selenium
# (1) - opção 2 : abir até a página máxima e não permitir salvar links repetidos 