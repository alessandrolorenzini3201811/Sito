const http = require('http');
const express = require('express')

const app = express()

// Crea un server HTTP
const server = http.createServer((req, res) => {
  // Imposta l'intestazione della risposta
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  // Invia una risposta al client
  res.end('Ciao, mondo!');
});

// Specifica la porta su cui il server deve ascoltare
const port = 3000;

// Avvia il server e ascolta sulla porta specificata
server.listen(port, () => {
  console.log(`Server in ascolto sulla porta ${port}`);
});