const express = require('express');
const app = express();
const port = 4000;
const { spawn } = require('child_process');


app.use(express.json());



app.post('/grafo', (req, res) => {
  let risposta='';
  const { transcription } = req.body;
  const {colore} = req.body
  const {lingua} =req.body
  console.log('Trascrizione:', transcription);
  const filename = 'grafoattdiff.json';

    const ls = spawn('python', ['grafotest.py', filename, transcription, colore,lingua]);
    ls.stdout.on('data', (data) => {
      console.log(`stdout: ${data.toString('utf-8')}`);
      risposta+=data;
      res.setHeader('Content-Type', 'application/json; charset=utf-8');
      res.send(JSON.stringify({ message: risposta }, null, 2));
    });
    ls.stderr.on('data', (data) => {
      console.log("test");
    });
 
});




app.listen(port, () => {
    console.log(`Server in ascolto sulla porta ${port}`);
  });