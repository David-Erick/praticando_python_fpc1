#Modalidade Programação • Nível Júnior • Fase 1
#Ano 2022

"""
Cinema
Nome do arquivo: cinema.c, cinema.cpp, cinema.pas, cinema.java, cinema.js ou cinema.py
Duas amigas estão na fila para comprar ingressos para uma sessão de cinema. O preço dos ingressos,
em Reais, é dado na tabela abaixo:
Idade Preço
até 17 anos 15
18 a 59 anos 30
60 anos ou mais 20
Dadas as idades das amigas, escreva um programa para calcular o total a ser pago pelos dois
ingressos.
Entrada
A entrada contém duas linhas, cada linha contendo um inteiro, a idade de uma das amigas.
Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, que deve ser o valor total
em Reais a ser pago pelos dois ingressos.
Restrições
• 1 ≤ idade ≤ 100
Exemplo de entrada 1
100
10
Exemplo de saída 1
35
Explicação do exemplo 1: Os valores dos ingressos para as idades 100 e 10 são respectivamente
20 e 15, portanto o total é 35.
Exemplo de entrada 2
17
18
Exemplo de saída 2
45
Explicação do exemplo 2: Os valores dos ingressos para as idades 17 e 18 são respectivamente
15 e 30, portanto o total é 45.
"""

totalIngresso = 0

#recebe as idades
for i in range(2):
    idade = int(input(f"digite a idade da amiga {i+1}: "))
    #restricoes
    if 1>= idade <= 100:
        break
    #determina o valor do ingresso de acordo com a idade
    if idade <= 17:
        totalIngresso += 15
    elif 18<= idade <= 59:
        totalIngresso += 30
    elif idade >= 60:
        totalIngresso += 20

print(f"o valor total a ser pego pelos dois ingressos é de: {totalIngresso} Reais")

