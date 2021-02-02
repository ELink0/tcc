#-*- coding: UTF-8 -*-
from random import randint
from random import random

texto_1 = "O Fulano de Tal e uma pessoa (legal, gente boa, simpatico) e de uma familia (boa, de pessoas educadas). Ele tambem e muito (trabalhador, criativo, educado).!"
texto_2 = "O Fulano de Tal e uma pessoa (chata, estranha, antipatico) e de uma familia (de pessoas mal educadas, estranha). Ele tambem e muito (preguicoso, oferecido, ruim).!"

controle_loop = 0
while controle_loop == 0:
			def gerarHash(texto):
				valor = 0
				max = 128
				for i in texto:
					valor += ord(i)

			 	hash = valor % max
			 	return hash

			def substituiTag(texto, adjetivos):
				textoNovo = ""
				z = 0
				estado = "fora"

				for i in texto:
					if estado == "fora":
						if i != "<":
							textoNovo += i
						else:
							sorteio = sortearAdjetivos(adjetivos)
							textoNovo += str(sorteio[z])
							estado = "dentro"

					elif estado == "dentro":
						if i == ">":
							estado = "fora"
							z += 1
				return textoNovo

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


			def sortearAdjetivos(adjetivos):
				novaLista = []

				for x in range(len(adjetivos)):
					z = randint(0, len(adjetivos[x])-1)
					novaLista.append(adjetivos[x][z])
				return novaLista

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

			sortearAdjetivos(adjetivos_1)
			sortearAdjetivos(adjetivos_2)

			# Chama a função de substituir Tags
			textoNovo1 = substituiTag(textoConvertido_1, adjetivos_1)
			textoNovo2 = substituiTag(textoConvertido_2, adjetivos_2)

			# Chama função de gerar Hash
			hash1 = gerarHash(textoNovo1)
			hash2 = gerarHash(textoNovo2)

			if hash1 == hash2:
				print("Bingo!", hash1, hash2)
				break


	# print(sortearAdjetivos(adjetivos_1))

	# permuta(adjetivos_2, [], 0)
	# adjetivosSorteados = sortearAdjetivos(adjetivos_1, 0)
