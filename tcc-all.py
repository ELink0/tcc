#-*- coding: UTF-8 -*-
import random

texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc). Ele também é muito (trabalhador, criativo, educado) faz parte de uma família (muito boa, excelente, renomada)"
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
	global textoConvertido

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

	return texto, textoConvertido


identificaParenteses(texto)
permuta(adjetivos, adjpermutados, 0)

# Texto 2 vai ter que receber pelo retorno da função
