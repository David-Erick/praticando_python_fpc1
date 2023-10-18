#Olimpíada Brasileira de Informática – OBI2021 – Prog. Nível Sênior – Fase Fase 1

#List comprehension que pega os resultados das partidas e armazena tudo dentro da lista de uma só vez
resultado = [str(input("Qual resultado da partida? V(venceu)  P(perdeu)")) for i in range(5)]
print(resultado)
partidasVencidas = 0

#Conta quantas vitorias o competidor teve
for valor in resultado:
    if valor == "v" or valor == "V":
        partidasVencidas += 1
   
#Aloca o competidor em seu determinado grupo de acordo com suas vitorias
if partidasVencidas >= 5:
    grupo = 1
elif partidasVencidas >= 3:
    grupo = 2
elif partidasVencidas >= 1:
    grupo = 3
else:
    grupo = -1

print(grupo)
