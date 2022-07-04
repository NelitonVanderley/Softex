import time
tempo = int(input('Informe o tempo para a contagem regressiva: '))
print('\n\nAtenção! \nIniciando contagem regressiva... ')
time.sleep(1)
def contagem_regressiva(tempo):
	for i in range(tempo, -1, -1):
		if i == 0:
			explosao = True
			break
		print(i)
		time.sleep(1)
	return explosao

if contagem_regressiva(tempo) == True:
	print("Buuum!!!!  \nA bomba explodiu!!!!") 


#Realiza a contagem regressiva para a explosão de uma bomba!