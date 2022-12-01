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
palavrasIniciais = ["Aureo","Coisa"] #Indas
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
sleep(5)

input_box = driver.find_element(By.TAG_NAME, "body")
input_box.click()


def digitar(palavra=choice(palavrasIniciais)):

  input_box.send_keys(palavra)
  input_box.send_keys(Keys.ENTER)

  sleep(1)


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

debug = True
palavraDebug = "corpo"
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
  vogais = ['a','e','i','o','u']

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
    etapa1 = True
    etapa2 = True
    etapa3 = True
    etapa4 = True
    etapa5 = True
    etapa6 = True

    if p in palavrasUsadas:
      
      etapa6 = False

    for x in lPE:
      if x not in p:
        if debug and p == palavraDebug:
          print("Falhou no LPE")
       
        etapa6 = False

    if p[1] == p[0] and p[1]  in vogais or p[2] == p[1] and p[2] in vogais or p[3] == p[2] and p[3] in vogais or p[4] == p[3] and p[4] in vogais:
      etapa6 = False

    for x in letrasCertas:
      if x not in p:
        if debug and p == palavraDebug:
          print("Falhou no lC")
          
        etapa6 = False

      else:
        for y in letrasCertas[x]:
          if int(y) not in findOccurrences(p,x):
            if debug and p == palavraDebug:
              print(y, findOccurrences(p,x))
              print("Falhou no lC2")
              
            etapa6 = False

    for x in p:
      if x in letrasErradas and x not in letrasCertas:
        if debug and p == palavraDebug:
          print("Falhou no lE")
        etapa6 = False
        
        

    if palavra[0] != " ":
      if p[0] != palavra[0]:
        etapa1 = False
      
      
    else:
      if p[0] in lPE and 0 in lPE[p[0]]:
        etapa1 = False
      
                  

    if palavra[1] != " ":
      if p[1] != palavra[1]:
        etapa2 = False
      
      
    else:
      if p[1] in lPE and 1 in lPE[p[1]]:
        etapa2 = False
      


    if palavra[2] != " ":
      if p[2] != palavra[2]:
        etapa3 == False
      
      
    else:
      if p[2] in lPE and 2 in lPE[p[2]]:
        etapa3 = False 
      

    if palavra[3] != " ":
      if p[3] != palavra[3]:
        etapa4 = False
      
      
    else:
      if p[3] in lPE and 3 in lPE[p[3]]:
        etapa4 = False
      

    if palavra[4] != " ":
      if p[4] != palavra[4]:
        etapa5 = False
      
      
    else:
      if p[4] in lPE and 4 in lPE[p[4]]:
        etapa5 = False

    
                       
    if p == palavraDebug and debug:
      print(f"Palavra -> {p}")
      print(f"Etapa 1 -> {etapa1}")
      print(f"Etapa 2 -> {etapa2}")
      print(f"Etapa 3 -> {etapa3}")
      print(f"Etapa 4 -> {etapa4}")
      print(f"Etapa 5 -> {etapa5}")
      print(f"Etapa 6 -> {etapa6}")
      print("--------------------------------------------")
      

    if  etapa1 == True and etapa2 == True and etapa3== True and etapa4 == True and etapa5 == True and etapa6 == True:
      
      if row ==2: 
        
        palavras1.append(p)
       
      elif row==3:
        
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
  
  

  

  if row == 2:
    p = choice(palavras1)
    
    digitar(p)
    palavrasUsadas.append(p)
        
  elif row == 3:
    p = choice(palavras2)

    digitar(p)
    palavrasUsadas.append(p)
        
  elif row == 4:
    p = choice(palavras3)

  
    digitar(p)
    palavrasUsadas.append(p)
        
  elif row == 5:
    p = choice(palavras4)
    digitar(p)
    palavrasUsadas.append(p)
        
  elif row == 6:
    p = choice(palavras5)
    digitar(p)
    palavrasUsadas.append(p)

    
  
      

    

# Fechar navegador
#driver.quit()