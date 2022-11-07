#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

cep = sys.argv[1]

if cep:

    driver = webdriver.Chrome('g_webdriver/chromedriver')

    #driver.get('https://caionosdados.com.br')
    #driver.get('https://uol.com.br')
    #driver.get('https://www.howedu.com.br')
    # driver.find_element("xpath", '//*[@id="btnCookie"]').click()
    sleep(2)
    # driver.find_element("xpath", '//*[@id="adopt-accept-all-button"]').click()



    #driver.get('https://correios.com.br/')

    #aceesando site dos correios

    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')


    element_cep = driver.find_element(By.NAME, 'endereco')
    element_cep.send_keys(cep)


    #selecionando comb box 
    element_comb = driver.find_element(By.NAME, 'tipoCEP').click()

    driver.find_element(By.XPATH, '//*[@id="tipoCEP"]/optgroup/option[6]').click()
    #driver.find_element(By.NAME, 'tipoCEP').click()
    driver.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()


    logradouro = driver.find_element(By.XPATH,
                                '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    rua = logradouro.split(' - ')[0]

    bairro = driver.find_element(By.XPATH,
                                '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text


    localidade = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text

    
    print(f"""
    Para o cep {cep} temos:
    Endereço: {rua}
    Bairro: {bairro}
    Localidade: {localidade}
    """)

    driver.close()

# %%
