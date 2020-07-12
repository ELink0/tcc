#-*- coding: UTF-8 -*-

texto_1 = "O Fulano de Tal e uma pessoa (legal, gente boa, simpatico) e de uma familia (boa, de pessoas educadas). Ele tambem e muito (trabalhador, criativo, educado).!"
texto_2 = "O Fulano de Tal e uma pessoa (chata, estranha, antipatico) e de uma familia (de pessoas mal educadas, estranha). Ele tambem e muito (preguicoso, oferecido, ruim).!"

# Somar os caracteres e somar o módulo da divisão
# Converter cada caracter para o código ASCII

def gerarHash(texto):
	valor = 0
	maximo = 1000
	for i in texto:
		valor += ord(i)
		valor = valor % maximo
		if valor >= maximo:
			valor = 1000


def permuta(adjetivos, adjpermutados, z):
	k = 0
	if len(adjetivos) == z:
		print k, ' ', adjpermutados
		k += 1

	else:
		for i in range(len(adjetivos[z])):
			nova_lista = list(adjpermutados)

			nova_lista.append(adjetivos[z][i])
			permuta(adjetivos, nova_lista, z+1)

def identificaParenteses(texto):
	textoConvertido = ""
	adjetivos = []
	adjetivo = ""
	estado = "fora"
	contador = 0
	linha = []

	for t in texto:
		if estado == "fora":
			if t != "(":
				textoConvertido += t

			else:
				textoConvertido += "<t"+str(contador)+">"
				linha = []
				estado = "dentro"
				adjetivo = ""

		elif estado == "dentro":
				if t == ")":
					estado = "fora"
					contador += 1
					linha.append(adjetivo)
					adjetivos.append(linha)

				elif t == ",":
					linha.append(adjetivo)					 
					adjetivo = ""

				else:
					adjetivo += t

	return adjetivos, textoConvertido

adjetivos_1, textoConvertido_1 = identificaParenteses(texto_1)
adjetivos_2, textoConvertido_2 = identificaParenteses(texto_2)

hash1 = gerarHash(texto_1)
hash2 = gerarHash(adjetivos_2)


# permuta(adjetivos_2, [], 0)
