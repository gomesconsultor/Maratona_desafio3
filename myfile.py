from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br")
res = BeautifulSoup(html.read(),"html5lib")
teste = res.title.getText()
separa = teste.split("|")
aux = separa[0].split(":")
author = aux[0].rstrip()
titulo = aux[1].lstrip()
print(author)
print(titulo)
tags = res.findAll("div", {"class": "Grid__cell flx-s:1 p-r:4"})
valor = ""
body= ""
for tag in tags:
    aux= ""
    aux2=""
    aux3=""
    valor="" 
    # print(tag.getText())
    aux = tag.getText()
    aux = aux.lstrip("\n\t") 
    aux2 = aux.replace("\n","")
    aux3  = aux2.replace("\t","")
    aux =  aux3.rstrip("\t")
    if (len(aux) > 3):
        valor = aux + "\n"
    # if (i == i * 3) :
        body = body + valor    
body = body    
print(body)