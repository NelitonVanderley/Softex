'''Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get) e um método modificador (set) para cada. Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.

A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos.'''


class Idade ():
	def __init__(self, ano_nasc, ano_atual):
		self.ano_nasc = ano_nasc
		self.ano_atual = ano_atual
		self.idade = 2022 - self.ano_nasc
	
	def get_ano_nasc(self):
		return self.ano_nasc

	def set_ano_nasc(self, novo_ano):
		self.ano_nasc = novo_ano

	def get_ano_atual(self):
		return self.ano_atual

	def set_ano_atual(self, novo_ano_atual):
		self.ano_atual = novo_ano_atual



idade = Idade(1990, 2022)	
print('O ano de nascimento é : ', idade.get_ano_nasc())

ano = int(input('Informe o ano de nascimento: '))
idade.set_ano_nasc(ano)
print('O novo ano de nascimento é: ', idade.get_ano_nasc())