from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from pyshadow.main import Shadow

from random import choice
from time import sleep

import unidecode

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
shadow = Shadow(driver)
palavras = []
palavrasIniciais = ["Aureo", "Indas"]
palavrasPossiveis = []
letrasErradas = []
letrasCertas = {}
letrasPosicionadasErradas = {}
palavrasUsadas = []

with open("palavras2.txt", mode="r") as file:
  for line in file.readlines():

    palavras.append(line.replace("\n", ""))

    pass

for x in palavras:
  if len(x) == 5:

    palavrasPossiveis.append(x)

driver.get('https://term.ooo/')

row = 1
sleep(10)

input_box = driver.find_element(By.TAG_NAME, "body")
input_box.click()


def digitar(palavra=choice(palavrasIniciais)):

  input_box.send_keys(palavra)
  input_box.send_keys(Keys.ENTER)

  sleep(3)


digitar()


def scrapper():
  return shadow.find_elements(
    "div[class='letter wrong']"), shadow.find_elements(
      "div[class='letter right']"), shadow.find_elements(
        "div[class='letter place']")


wrong, right, place = scrapper()


def organizador():

  for x in wrong:

    if unidecode.unidecode(x.text.lower()) in letrasErradas:
      continue
    else:
      letrasErradas.append(unidecode.unidecode(x.text.lower()))

  for x in right:

    if unidecode.unidecode(x.text.lower()) in letrasCertas:
      pos = x.get_attribute("lid")
      letrasCertas[unidecode.unidecode(x.text.lower())].append(pos)
    else:
      pos = x.get_attribute("lid")
      letrasCertas[unidecode.unidecode(x.text.lower())] = [pos]

  for x in place:

    if unidecode.unidecode(x.text.lower()) in letrasPosicionadasErradas:
      pos = x.get_attribute("lid")
      if pos in letrasPosicionadasErradas[unidecode.unidecode(x.text.lower())]:
        pass

      else:
        pos = x.get_attribute("lid")
        letrasPosicionadasErradas[unidecode.unidecode(
          x.text.lower())].append(pos)

    else:
      pos = x.get_attribute("lid")
      letrasPosicionadasErradas[unidecode.unidecode(x.text.lower())] = [pos]


palavra = "     "

palavras1 = []
palavras2 = []
palavras3 = []
palavras4 = []
palavras5 = []


def EscolherPalavras(lCertas=letrasCertas,
                     lErradas=letrasErradas,
                     lPE=letrasPosicionadasErradas):
  global row
  global palavra

  if len(lCertas) >= 1:
    for x, y in lCertas.items():
      for z in y:

        s = list(palavra)
        s[int(z)] = x
        palavra = "".join(s)

  def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

  row += 1
  for p in palavrasPossiveis[:]:
    etapa1 = False
    etapa2 = False
    etapa3 = False
    etapa4 = False
    etapa5 = False

    if palavra[0] != " ":
      if palavra[0] == p[0]:
        etapa1 = True
      pass
    else:
      if p[0] in letrasErradas:
        pass
      elif p[0] in letrasPosicionadasErradas and p[
          0] in letrasPosicionadasErradas[p[0]]:
        pass
      else:
        etapa1 = True

    if palavra[1] != " ":
      if palavra[1] == p[1]:
        etapa2 = True
      pass
    else:
      if p[1] in letrasErradas:
        pass
      elif p[0] in letrasPosicionadasErradas and 0 in letrasPosicionadasErradas[
          p[0]]:
        pass
      else:
        etapa2 = True

    if palavra[2] != " ":
      if palavra[0] == p[2]:
        etapa3 = True
      pass
    else:
      if p[2] in letrasErradas:
        pass
      elif p[1] in letrasPosicionadasErradas and 1 in letrasPosicionadasErradas[
          p[1]]:
        pass
      else:
        etapa3 = True

    if palavra[3] != " ":
      if palavra[3] == p[3]:
        etapa4 = True
      pass
    else:
      if p[3] in letrasErradas:
        pass
      elif p[2] in letrasPosicionadasErradas and 2 in letrasPosicionadasErradas[
          p[2]]:
        pass
      else:
        etapa4 = True

    if palavra[4] != " ":
      if palavra[4] == p[4]:
        etapa5 = True
      pass
    else:
      if p[4] in letrasErradas:
        pass
      elif p[3] in letrasPosicionadasErradas and 3 in letrasPosicionadasErradas[
          p[3]]:
        pass
      else:
        etapa5 = True
    for x in letrasPosicionadasErradas:
      if x not in p:
        etapa5 = False

    if p in palavrasUsadas:
      etapa5 = False

    if  etapa1 and etapa2 and etapa3 and etapa4 and etapa5:
      if row ==2: 
        
        palavras1.append(p)
       
      elif row==3:
        print(p)
        palavras2.append(p)
      elif row==4:
        palavras3.append(p)
      elif row==5:
        palavras4.append(p)
      elif row==6:
        palavras5.append(p)
              

    
    


while row <= 5:

  wrong, right, place = scrapper()
  organizador()

  EscolherPalavras()

  retries = 0

  if row == 2:
        

    digitar(choice(palavras1))
        
  elif row == 3:

    digitar(choice(palavras2))
        
  elif row == 4:
    digitar(choice(palavras3))
        
  elif row == 5:
    digitar(choice(palavras4))
        
  elif row == 6:
    digitar(choice(palavras5))

    
  
      

    

# Fechar navegador
#driver.quit()