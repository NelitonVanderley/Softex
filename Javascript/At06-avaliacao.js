function programa1 (){
	function situacaoAluno (notaacumulada) {
		media = notaacumulada / 3
		media >= 7 ? situacao = 'APROVADO' : situacao = 'REPROVADO'
		
		return situacao
	}
		
	var notaacumulada = 0
	var nota1 = Number(prompt('Informe a primeira nota do aluno: '))
	notaacumulada += nota1
	var nota2 = Number(prompt('Informe a segunda nota do aluno: '))
	notaacumulada+=nota2
	var nota3 = Number(prompt('Informe a terceira nota do aluno: '))
	notaacumulada += nota3
	situacaoAluno(notaacumulada)
	alert('O aluno está '+ situacao + "!")
}

function programa2() {
	function situacao(nota){
		media = 7
		notaRestante = (3* media) - nota    
		return notaRestante
	}
	var nota = 0
	var nota1 = Number(prompt('Informe sua primeira nota: '))
	nota += nota1
	var nota2 = Number(prompt('Informe sua segunda nota: '))
	nota += nota2
	situacao(nota)
	alert('Você precisa de uma nota igual ou maior a ' + notaRestante)
	
}
var sistema = prompt('Informe qual programa deseja inicializar: Digite 1 ou 2')
switch (sistema) {
	case '1':
		programa1()
	break;
	case '2':
		programa2()
	break;	

	default:
		break;
}

