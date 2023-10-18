#Olimpíada Brasileira de Informática – OBI2020 – Prog. Nível Júnior – Fase Local (Piloto Automatico)

posCarroA = int(input("Qual a posição do carro A?  "))
posCarroB = int(input("Qual a posição do carro B?  "))
posCarroC = int(input("Qual a posição do carro C?  "))

media = (posCarroA + posCarroC)/2

if media == posCarroB:
    resultado = 0

elif media >  posCarroB:
    resultado = 1

elif media < posCarroB:
    resultado = -1

print(resultado)