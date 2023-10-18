# Olimpíada Brasileira de Informática – OBI2021 (Idade de Camila)

#List comprehension que pega as idades das irmas
idades = [int(input(f"Digite a idade da irma {i+1}:  ")) for i in range (3)]
idades.sort()

#valida as idades e estando validas, retorna a idade de Camila
if 4 >= idades[0] or idades[2] >=101:
    print("idades invalidas")
else:
    print(idades[1])

