lista = ['a', 'b', 'c']
lista1 = ''
k = 0

def permuta(lista, lista1, z):
	global k
	if len(lista) == z:
	    # assim que o processo do FOR abaixo for finalizado, será imprimido aqui 
	    # os elementos da lista1, que são os que foram permutados
		print k, lista1
		k += 1
		
	else:
	    # Nesta parte nós vamos estar percorrendo a nossa matriz
	    # e a cada iteração do for vamos estar adicionando o elemento i 
	    # na lista1
	    # para cada elemento percorrido da lista vai ser adicionado ao lista1
		for i in range(len(lista)):
			permuta(lista, lista1+lista[i], z+1)
        
permuta(lista, lista1, 0)
