function Carro (marca, ano, valor){
	this.marca = marca;
	this.ano = ano;
	this.valor = valor
}

var ferrari = new Carro('Ferrari', 2020, 1000000)
var gol = new Carro('Gol', 2012, 10000)
var fusca = new Carro('Fusca', 1989,1000)

var marcas = ['ferrari', 'gol', 'fusca']

var exibirObjetos = (Carro) => {
	for (var c in ferrari) {
		console.log(c)
	}  


}