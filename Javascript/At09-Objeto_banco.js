class Banco {
	constructor (numConta, saldo, tipoConta, agencia) {
	this.numConta = numConta;
	this.saldo = saldo;
	this.tipoConta = tipoConta;
	this.agencia = agencia;
	}
		mostrarsaldo (){
	
			return console.log(`Conta: ${this.numConta}. Ag ${this.agencia}. Saldo atual ${this.saldo}`)
		}
		deposito (valordeposito){
			this.saldo += valordeposito
			
			return console.log(`Conta: ${this.numConta}. Ag ${this.agencia}. Valor depositado ${valordeposito}. Saldo atual ${this.saldo}`)
		}
		saque (valorsaque){
			this.saldo -= valorsaque
			return console.log(`Conta: ${this.numConta}. Ag ${this.agencia}. Valor sacado ${valorsaque}. Saldo atual ${this.saldo}`)
		}
		numeroConta (){
			return console.log(`Conta: ${this.numConta}. Ag ${this.agencia}.`)
		}

}
var conta = new Banco ('001',0, 'cc', "001")

conta.deposito(2000)
conta.saque(500)
conta.mostrarsaldo()
conta.deposito(200)
conta.numeroConta()
conta.mostrarsaldo()

var conta2 = new Banco ('002',0, 'cc', "001")

conta2.deposito(5000)
conta2.saque(1000)
conta2.mostrarsaldo()
conta2.deposito(2200)
conta2.numeroConta()
conta2.mostrarsaldo()