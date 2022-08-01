/*Crie um programa que contenha os seguintes tipos de funções:

1. uma função tradicional com a palavra reservada “Function” e sem nenhum parâmetro;
2. uma função tradicional com parâmetros e um retorno de valor;
3. uma arrow function com parâmetros e que retorne um valor.

Crie um programa que utilize essas três funções de forma lógica, por exemplo: um programa de calculadora.*/


function iniciar (){
	var boas_vindas = `Olá! Bem vindos ao programa!`

	return boas_vindas
}

function soma (num1, num2){
	resultado = num1 + num2

	return resultado
}

const subtrair = (num1, num2)=> num1 - num2 


iniciar()
soma(10,2)
subtrair(10, 9)