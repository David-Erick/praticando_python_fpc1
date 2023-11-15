saida = 0
qtd_pessoas = int(input())
qtd_bolos = int(input())
#divide em valores inteiros o comprimento de cada bolo
comprimento_bolos = [int(tamanho) for tamanho in input().split()]
maior_elem_lista = max(comprimento_bolos)
#divide todo elemento da lista por i (que está em um range do maior valor de comprimento de bolo até 1)
#uma vez que a soma dessa nova lista for igual a qts_pessoas, ele retorna o valor de i
for i in range(maior_elem_lista, 1, -1):
    resultado = [x // i for x in comprimento_bolos]
    if sum(resultado)==qtd_pessoas:
        saida = i
        break
    else:
        continue
print(saida)
