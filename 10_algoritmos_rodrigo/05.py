#Olimpíada Brasileira de Informática – OBI2019 – Prog. Nível Júnior – Fase Local (Idade da dona monica)

idadeDM = int(input("digite a idade de Dona monica:  "))
idadeF1 = int(input("digite a idade do filho 1:  "))
idadeF2 = int(input("digite a idade do filho 2:  "))

#calculo para achar a idade do terceiro filho
idadeF3 = idadeDM - (idadeF1 + idadeF2)

idades = [idadeF1, idadeF2, idadeF3]

#ordena as idades me ordem crescente 
idades.sort()
print(idades[2])