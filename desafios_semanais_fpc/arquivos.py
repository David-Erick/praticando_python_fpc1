#list comprehensiuon que recebe as entradas N e B
entrada = [int(valor) for valor in input().split()]
#atribuindo as variaveis de acordo com a lista
qtdArquivos, tamanho_cada_arquivo = entrada
#list comprehension que recebe o tamanho de cada arquivo
arquivos= [int(arq) for arq in input().split()]
#print do resultado fazendo o calculo com a soma da lista "arquivos" dividido pelo tamanho de cada arquivo
print(int(sum(arquivos)/tamanho_cada_arquivo))
