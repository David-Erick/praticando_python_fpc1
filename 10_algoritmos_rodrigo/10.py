#Olimpíada Brasileira de Informática – OBI2021 – Prog. Nível Júnior – Fase Fase 3 (Ogro)

dedosLevantado = int(input("Quantos dedos o ogro deve levantar?  "))
lista=[]
lista2=[]
for i in range(dedosLevantado):
    lista.append("I")
    if len(lista) == 5:
        break
dedosRestantes = dedosLevantado - 5

for i in range(dedosRestantes):
    lista2.append("I")

if dedosRestantes == 0:
    lista2.append("*")

print(lista)
print(lista2)
