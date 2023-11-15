saida = 0
qtd_pessoas = int(input())
qtd_bolos = int(input())
#divide em valores inteiros o comprimento de cada bolo
comprimento_bolos = [int(tamanho) for tamanho in input().split()]
maior_elem_lista = max(comprimento_bolos)

for i in range(maior_elem_lista, 1, -1):
    resultado = [x // i for x in comprimento_bolos]
    if sum(resultado)==qtd_pessoas:
        saida = i
        break
    else:
        continue
print(saida)
