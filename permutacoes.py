matriz_adjs = [['a', 'b', 'c'], ['0', '1', '3', '4']]
lista1 = ''
k = 0

def permuta(matriz, lista1, z):
	global k
	if len(matriz) == z:
		# assim que o processo do FOR abaixo for finalizado, sera imprimido aqui 
		# os elementos da lista1, que so os que foram permutados
		print k, ' ', lista1
		k += 1
		
	else:
		# Nesta parte nos vamos estar percorrendo a nossa matriz
		# e a cada iteracao do for vamos estar adicionando o elemento i 
		# na lista1
		# para cada elemento percorrido da lista vai ser adicionado ao lista1
		for i in range(len(matriz[z])):
			permuta(matriz, lista1+' '+matriz[z][i], z+1)
        
permuta(matriz_adjs, lista1, 0)


# o prof eduardo eh <t0> e o sei la o que eh <t1>
