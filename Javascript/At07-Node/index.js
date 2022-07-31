function somar (num1, num2){
	resultado = num1 + num2;
	alert('O resultado da operação é: ' + resultado)
}

function subtrair (num1, num2){
resultado = num1 - num2
alert('O resultado da operação é: ' + resultado)
}	

function multiplicar (num1, num2){
	resultado = num1 * num2
	alert('O resultado da operação é: ' + resultado)
}		

function dividir (num1, num2){
	if (num2 == 0){
		alert('Não é possível realizar a divisão por zero!')
	}
		else{
			resultado = num1 / num2
			resto = num1%num2
			if (resto!=0){
			alert('O resultado da operação é: ' + resultado + ' e o resto da divisão é: ' + resto)
			}
				else{
					alert('O resultado da operação é: ' + resultado)
				}
		}
}	
while(true){
		var num1 = Number(prompt('Informe o primeiro número: '))
		var operador = prompt('Informe a operação: ')
		var num2 = Number(prompt('Informe o segundo número: '))

		if (operador == '+'){
			somar(num1, num2)
		}
			else if  (operador == '-'){
				subtrair(num1, num2)
			}
				else if  (operador == '*'){
					multiplicar(num1, num2)
				}
					else if  (operador == '/'){
						dividir(num1, num2)
					}
						else{ alert('Operação inválida!')
						}
}