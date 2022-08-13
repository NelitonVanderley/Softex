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