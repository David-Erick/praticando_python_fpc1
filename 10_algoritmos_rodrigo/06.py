D = int(input("Qual a distancia do robo ate o inicio da quadra?  "))

#compara a distancia jogada e determina a pontuação
if D <= 800:
    valorCesta = 1
elif 800 < D <= 1400:
    valorCesta = 2
elif 1400 < D <= 2000:
    valorCesta = 3
else:
    valorCesta = 0

print(valorCesta)