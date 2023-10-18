#Olimpíada Brasileira de Informática – OBI2021 – Prog. Nível Júnior – Fase Fase 2 (Turno B) (Recorde)

r = int(input("Qual o melhor resultado obtido por um atleta numa prova das olimpiadas  "))
m = int(input("Qual o recorde mundial para essa prova?  "))
l = int(input("Qual o recorde olimpico para essa prova?  "))

#compara o resultado com o recorde mundial
if r > m:
    resultado = "RM"
    print(resultado)
else:
    print("*")

#compara o resultado com o recorde olimpico
if r > l:
    resultado = "RO"
    print(resultado)
else:
    print("*")