totalFig = int(input("Digite o numero total de figurinhas do album:  "))
totalCompr = int(input("Digite o tital de figurinhas ja compradas:  "))

#list comprehesion que guarda as figurinhas já compradas
listaJaCompr = [int(input("Digite uma fogurinha que ja tem:  ")) for i in range(totalCompr)]
#calcula o total de figurinhas faltando
totalFalta = totalFig - totalCompr

print(totalFalta)