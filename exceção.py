#exceção
#Crie uma situação em que ocorra uma exceção dentro de um código. Utilize try/catch para realizar a captura e tratamento dessa exceção. 

def divisao():
	try:
		num1 = int(input('Informe um número: '))
		num2 = int(input('Informe por quanto deseja dividir número informado anteriormente: '))
		resultado = num1 / num2
		print('O resultado da divisão é: ', resultado, ' !')

	except:
		print('valor informado não corresponde a um número válido.')
divisao()
