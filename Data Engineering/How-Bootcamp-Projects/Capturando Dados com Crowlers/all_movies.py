#%%
import os
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('g_webdriver/chromedriver')
driver.implicitly.wait(3)
wikipedia = driver.get('https://pt.wikipedia.org/wiki/Samuel_L._Jackson')
table = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]')
print(table.get_attribute("innerHTML"))

df = pd.read_html('<table>' + table.get_attribute('innerHTML') + '</table>')[0]
#%%
def tem_intem(xpath: str, driver =driver):
    driver.find_element(By.XPATH, xpath)



#%%
df
#%%
df.Ano.values

# %%
df[df['Ano'] == '1972']

