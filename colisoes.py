retangulo1 = input("Digite os pontos do primeiro retângulo (x0 y0 x1 y1):  ")
retangulo2 = input("Digite os pontos do segundo retângulo (x2 y2 x3 y3):  ")

#utiliza list comprehension para transformar os valores das entradas para inteiro e sepra-los
retangulo1 = [int(ponto) for ponto in retangulo1.split()]
retangulo2 = [int(ponto) for ponto in retangulo2.split()]

x0, y0, x1, y1 = retangulo1
x2, y2, x3, y3 = retangulo2

#verifica se os retangulos se encostam no eixo X
encostaX = x0 < x3 and x1 > x2
#verifica se os retangulos se encostam no eixo Y
encostaY = y0 < y3 and y1 > y2

#retorna o resultado dependendo de se eles se encostam ou não
if encostaX and encostaY:
    resultado = 1
else:
    resultado = 0

print(resultado)
