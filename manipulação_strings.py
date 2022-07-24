#Manipulação de Strings

palavra = input('Informe uma palavra: ')

def maiusculo (palavra):
	palavra = palavra.upper() 

	print('Palavra com todos os caracteres maiúsculos: ', palavra)

def minusculo (palavra):
	palavra = palavra.lower()
	print('Palavra com todos os caracteres minúsculos: ', palavra)


def num_carcteres(palavra):
	num = len(palavra)
	print('A palavra informada possui ',num, 'letras')

maiusculo(palavra)
minusculo(palavra)
num_carcteres(palavra)