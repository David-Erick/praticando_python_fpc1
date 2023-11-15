lista = []
#funcao responsavel pela formula recursiva
def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return f(n/2)
    else:
        return f(3*n+1)
#funcao que retorna o numero de chamadas recursivas
def g(n, chamadas_recursivas=0):
    if n ==1:
        return chamadas_recursivas
    elif n%2 ==0:
        return g(n/2, chamadas_recursivas+1)
    else:
        return g(3*n+1, chamadas_recursivas+1)

num_casos_teste = int(input())

#recebe os valores a serem comparados 
for i in range(num_casos_teste):
    entradaXeY = [int(valor) for valor in input().split()]
    x, y = entradaXeY
#pega todos os valores das chamadas recursivas, e os ordena em uma lista para saber o maior
    for i in range(x, y+1):
        lista.append(g(i))
        lista.sort()
    print(lista[-1] + 1)
    lista = []
