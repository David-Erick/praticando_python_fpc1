#funcao que calcula da maneira iterativa o valor de fib(n)
def fib(n):
    a, b = 0, 1
    for i in range(2, n+1):
        r = a + b
        a, b = b, r
    return r
#funcao que calcula o numero de chamdas recursivas
def numRecursivas(n):
    a, b = 0, 2
    if n==2:
        return 2
    if n==1 or n==0:
        return 0
    
    for elem in range(1,n-1):
        num_recursivas =a + b + 2 #adiciono mais 2 pois o codigo desconsidera primeira chamamada
        a, b = b, num_recursivas
    return num_recursivas

casos_teste = int(input())

for i in range(casos_teste):
    valor_fib = int(input())

    fib(valor_fib)
    
    print(f"fib({valor_fib}) = {numRecursivas(valor_fib)} calls = {fib(valor_fib)}")
  
