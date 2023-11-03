numPecas = int(input("Quantas pecas tem o quebra cabeca? "))
listaDeNumeros =[]
qtd = numPecas 
while (numPecas-1) > 0:
    peca = int(input(f"digite a {numPecas-1}° peca: "))
    listaDeNumeros.append(peca)
    numPecas -= 1

for i in range(1, qtd+1 ):
    pertence = False
    for j in listaDeNumeros:
        if i == j:
            pertence = True           
    if not pertence:
        print(i)
        
   

