x = 0 #889
y = 0 #847
z = 0 #515
branco = 0
nulo = 0
finalizar = False
while finalizar == False:	
	for voto in range(0, 1, 1):
		try:
			voto = int((input('Informe o número do seu candidato: ')))
			if voto == 889:
				x = x +1
			elif voto == 847:
				y = y + 1
			elif voto == 515:
				z = z + 1
			elif voto == 0:
				branco = branco + 1
			else: nulo = nulo + 1

			finalizar = int(input('Deseja encerrar a votação?\nDigite: \n1 para Sim \n2 para Não\n'))
		except: 
			continue

	if finalizar == 2:
		finalizar = False
	elif finalizar == 1:
		if x > y and x > z:
			print('O vencedor foi o cadidado X com '+ str(x) + 'votos!')
			print('Votos Candidato Y '+ str(y))
			print('Votos Candidato Z '+ str(z))
			print('Votos Brancos e Nulos '+ str(branco+nulo))
			