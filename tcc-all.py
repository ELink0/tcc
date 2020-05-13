#-*- coding: UTF-8 -*-
import random

texto_1 = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatico) é de uma família (boa, de pessoas educadas). Ele também é muito (trabalhador, criativo, educado).!"
texto_2 = "O Fulano de Tal é uma pessoa (chata, estranha, antipático) é de uma família (de pessoas mal educadas, estranha). Ele também é muito (preguiçoso, oferecido, ruim).!"
adjetivos = []
adjpermutados = []
textoConvertido = ""


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


identificaParenteses(texto_1)
print(textoConvertido)
