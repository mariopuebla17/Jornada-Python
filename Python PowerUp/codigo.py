""" Passo a passo do projeto
Passo 1: entrar no sistema da empresa
Passo 2: logar no sistema
Passo 3: importar a base de dados
Passo 4: cadastrar um produto
Passo 5: repetir até acabar a base de dados
"""

import pyautogui #pip install pyautogui
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# pressionar uma tecla -> pyautogui.press

# Passo 1
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
time.sleep(1)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("teste@teste.com")
pyautogui.press("tab")
pyautogui.write("teste")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3
import pandas #pip install pandas numpy openpyxl

tabela = pandas.read_csv("produtos.csv")

# Passos 4 e 5
for linha in tabela.index:
    pyautogui.press("tab")
    # código
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    # preço unitário
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    pyautogui.press("enter")