#funcao que calcula o mdc de forma recursiva
def mdc(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return mdc(a, b) 


qtdTrocar = []
valido = False

#verica se o numero de trocas esta com a restricao indicada pelo exercicio
while valido == False:
    num_trocas = int(input(""))
    if 1 <= num_trocas<= 3000:
        valido = True

#recebe a quantidade de figurinhas de ricardo e vicente com um list comprehension
#e calcula a quantidade que sera trocada a partir do mdc entre elas
for i in range (num_trocas):
    qtdFig = [int(valor) for valor in input("Digite a quantidade de figurinhas: ").split()]

#verifica se o a quantidade de figurinhas eh valida
    if  1 <= qtdFig[0] <=1000 and 1<= qtdFig[1] <= 1000:
        qtdTrocar.append(mdc(qtdFig[0], qtdFig[1]))
    else:
        #print("invalido")
        break

#faz o print das saidas
for elem in range(len(qtdTrocar)):
    print(qtdTrocar[elem])
