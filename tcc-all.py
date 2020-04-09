#-*- coding: UTF-8 -*-
import random

texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc). Ele também é muito (trabalhador, criativo, educado) faz parte de uma família (muito boa, excelente, renomada)"
adjetivos = []
adjpermutados = []

linha = []

k = 0
textoConvertido = ""

textoConverte = []

def permuta(adjetivos, adjpermutados, z):
	global k
	if len(adjetivos) == z:
		print k, ' ', adjpermutados
		k += 1

	else:
		for i in range(len(adjetivos[z])):
			nova_lista = list(adjpermutados)

			nova_lista.append(adjetivos[z][i])
			permuta(adjetivos, nova_lista, z+1)
	return adjetivos, adjpermutados

def converteTexto(adjetivos, textoConverte):
	x = 0

	for i in texto:
		if i == "(":
			leitorTexto = textoConverte.append("<")
			leitorTexto = textoConverte.append("t")
			x += 1

		if i == ", ":
			leitorTexto = textoConverte.append("")

		if i == ")":
			leitorTexto = textoConverte.append(">")
			x = 0

		if x > 0:
			x =+ 1

		else:
			leitorTexto = textoConverte.append(i)
	return adjetivos, textoConverte

def identificaParenteses(adjetivos, linha, textoConvertido):
	adjetivo = ""
	estado = "fora"
	contador = 0


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

	return adjetivos, linha, textoConvertido


identificaParenteses(adjetivos, linha, textoConvertido)
converteTexto(adjetivos, textoConverte)
permuta(adjetivos, adjpermutados, 0)
