##Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def calculadora_idade (nome, ano_nasc):
	ano_atual = 2022
	idade = ano_atual - ano_nasc
	resposta = '{} em 2022 você fez ou fará {} anos.'.format(nome, idade)
	return resposta
	
nome = str(input('Informe seu nome completo: '))
erro = True
while erro ==True:
	try:
		ano_nasc = int(input('Informe o seu ano de nascimento: '))
		if ano_nasc >= 1922 and ano_nasc <= 2021:
			print(calculadora_idade(nome, ano_nasc))
			erro = False
		else:
			print('Ano de nascimento informado é invalido!')
			erro = True
	except: 
		print('Informação inválida!')
		erro = True






