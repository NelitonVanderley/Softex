print('Bem vendo a Calculadora!!\n------------------------------------------------------\n\n')
num1 = float(input('INFORME O PRIMEIRO NÚMERO: '))
num2 = float(input('\nINFORME O SEGUNDO NÚMERO: '))
operacao = int(input ('\nINFORME A OPERAÇÃO QUE SERÁ REALIZADA: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão \n'))

def calculadora(num1, num2, operacao):
	if operacao == 1:
		resultado = num1 + num2
	elif operacao == 2:
		resultado = num1 - num2
	elif operacao == 3:
		resultado = num1 * num2
	elif operacao == 4:
		resultado = num1 / num2
	else:
		resultado = 0
	return resultado

resultado = str(calculadora(num1, num2, operacao))
print('O resultado é igual a ' + resultado + ' !\nFim da operação')

