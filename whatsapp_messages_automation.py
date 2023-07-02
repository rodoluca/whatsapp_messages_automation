#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com")

Wait for the WhatsApp screen to load
while len(browser.find_elements(By.ID, 'side')) < 1:
time.sleep(1)
time.sleep(2) # Just to be sure


# In[ ]:


import pandas as pd

table = pd.read_excel("Envios.xlsx")
display(table[['nome', 'mensagem', 'arquivo']]) # There is also a 'telefone' column in the table


# In[ ]:


import urllib
import time
import os

for row in table.index:
    # Send a message to the person
    name = table.loc[row, "nome"]
    message = table.loc[row, "mensagem"]
    file = table.loc[row, "arquivo"]
    phone = table.loc[row, "telefone"]
    
    text = message.replace("fulano", name)
    text = urllib.parse.quote(text)

    # Send the message
    link = f"https://web.whatsapp.com/send?phone={phone}&text={text}"

    navegador.get(link)
    # Wait for the WhatsApp screen to load -> wait for an element that only appears when the screen is already loaded
    while len(navegador.find_elements(By.ID, 'side')) < 1: # If the list is empty, it means the element doesn't exist yet
        time.sleep(1)
    time.sleep(2) # Just to be sure

    # You have to check if the number is invalid
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        # Send the message
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

        if file != "N":
            full_path = os.path.abspath(f"arquivos/{file}")
            navegador.find_element(By.XPATH, 
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
            navegador.find_element(By.XPATH, 
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(full_path)
            time.sleep(2)
            navegador.find_element(By.XPATH, 
                                   '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()

        time.sleep(5)

