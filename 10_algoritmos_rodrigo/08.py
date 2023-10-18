#Olimpíada Brasileira de Informática – OBI2017 (Bondinho)

numAlunos = int(input("Digite o numero de alunos:  "))
numMoniotres = int(input("Digite o numero de monitores:  "))

if (numAlunos + numMoniotres) > 50:
    resultado = "N"
else:
    resultado = "S"

print(resultado)