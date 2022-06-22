class NumeroComplexo: 
	def interacao():
		global a, b, c, d, e, f
		a = int(input("Informe a parte real do primeiro número: "))
		b = int(input("Informe a parte imaginaria do primeiro número: "))
		c = int(input("Informe a parte real do segundo número: "))
		d = int(input("Informe a parte imaginaria do segundo número: "))
		e = int(input("Informe a parte real do terceirro número: "))
		f = int(input("Informe a parte imaginária do terceriro número: "))

	def  criacao_num_complexos(a, b, c, d, e, f):
		global num1, num2, num3
		num1 = complex(a,b)
		num2 = complex(c,d)
		num3 = complex(e,f)
		return print("Primeiro número complexo: {}\nSegundo número complexo: {}\nTerceiro número complexo: {}\n\n" .format(num1, num2, num3))

	def operacoes_numeros_complexos (num1, num2, num3):
		soma = num1 + num2 + num3
		subtracao = num1 - num2 - num3;
		multiplicacao = num1 * num2 * num3;
		divisao = num1 / num2 / num3
		return	print("A soma entre todos os números complexos é: {}\nA subtração entre todos os números complexos é: {}\nA multiplicação entre todos os números complexos é: {}\nA divisão entre todos os números complexos é: {}\n\n" .format(soma, subtracao, multiplicacao, divisao))

	def imprime_propriedades(num1,num2, num3):
		prop_num1 = num1
		prop_num2 = num2
		prop_num3 = num3
		return print("Propriedade real do primeiro número complexo: {} \nPropriedade imaginária do primreiro número complexo {}\n\nPropriedade real do segundo número complexo: {}\nPropriedade imaginária do segundo número complexo {}\n\nPropriedade real do terceiro número complexo: {} \nPropriedade imaginária do terceiro número complexo {}" .format(prop_num1.real, prop_num1.imag, prop_num2.real, prop_num2.imag, prop_num3.real, prop_num3.imag)) 

	
	interacao()
	criacao_num_complexos(a, b, c, d, e, f)
	operacoes_numeros_complexos(num1, num2, num3)
	imprime_propriedades(num1,num2, num3)
