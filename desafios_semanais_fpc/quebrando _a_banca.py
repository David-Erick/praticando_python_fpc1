#deixei o codigo espacado para melhor compreencao
while True:
    try:
        caracteres_total_apagados = [int(valor) for valor in input().split()]
        
        total, apagados = caracteres_total_apagados
        
        caracteres = int(input())
        
        lista_caracteres = list(str(caracteres))
        
        lista_caracteres = [int(valor) for valor in lista_caracteres]
        
        lista_caracteres.sort()
        
        lista_caracteres = lista_caracteres[apagados:]
        
        lista_caracteres = lista_caracteres[::-1]
        
        lista_caracteres = [str(numero) for numero in lista_caracteres]
        
        for i in range(len(lista_caracteres)):
            lista_concatenada = ''.join(lista_caracteres)
            print(lista_concatenada)
        
    except ValueError:
        break