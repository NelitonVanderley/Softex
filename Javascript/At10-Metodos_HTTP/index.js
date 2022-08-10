const http = require('http')
const express = require('express');
const app = express()
var rotas = require('./rotas')
app.use('/', rotas)

http.createServer(app).listen(3000, () => console.log("Servidor rodando local na porta 3000"));