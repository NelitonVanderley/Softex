const express = require('express');
const router = express.Router()

router.use(express.json());

var pessoas = []

router.get('/', (request, response) => {
	response.send('<h1> Servidor rodando com ExpressJS </h1>')
})

router.post('/enviar', (request, response) => {
	const {nome, idade} = request.body;
	const usuario = {
		nome,
		idade,
	};
	pessoas.push(usuario);
	console.log(pessoas)
	let retornoJson = response.json(usuario);

	return response.send(retornoJson.nome);
})

router.get('/listar', (request, response) => {
	response.send(pessoas)
})
module.exports = router
