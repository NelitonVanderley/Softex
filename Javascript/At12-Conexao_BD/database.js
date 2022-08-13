/*Implemente e trate uma conexão com o seu banco de dados, usando JavaScript. Caso a conexão com o banco tenha sucesso, ele deve retornar uma frase positiva. Se isso não ocorrer, retorne uma frase informando o erro.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.*/

const Sequelize = require('sequelize');
const sequelize = new Sequelize ('projeto_sequelize', 'root', 'Senha',{host: "localhost",
	dialect:'mysql'});
sequelize.sync().then(function() {
	console.log('Conexão com MySQL foi estabelecida com sucesso')
}) 
.catch((err) => {
	console.log('Não foi possivel conectar')
}) 
module.exports = sequelize