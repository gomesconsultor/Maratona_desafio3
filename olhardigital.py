from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683")
res = BeautifulSoup(html.read(),"html5lib")
teste = res.title.getText()
separa = teste.split("|")
print(teste)
lista = res.find("div", {"class": "mat-txt"})
tags =  lista.findAll('p')
body = ""
i = 0
for tag in tags:
    i = i + 1
    print(i)
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