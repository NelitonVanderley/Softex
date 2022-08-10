function Carro (marca, ano, valor){
	this.marca = marca;
	this.ano = ano;
	this.valor = valor
}

var palio = new Carro('Fiat', 2006, 15000)
var ferrari = new Carro('Ferrari', 2020, 1000000)
var gol = new Carro('Volkswagen', 2012, 10000)
var fusca = new Carro('Volkswagen', 1989,1000)

var marcas = [ferrari.marca, gol.marca, fusca.marca, palio.marca]

var exibirParametros = () => {
	for (var c in ferrari) {
		console.log('Propriedade do objeto: ' + c)
	} 
}
var exibiArray = () => {
    for ( var array of marcas){
        console.log('Marca: ' + array)
    }
}
exibirParametros()
exibiArray()
