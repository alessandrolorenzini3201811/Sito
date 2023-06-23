const express = require('express');
const app = express();
const port = 5000;
const { spawn } = require('child_process');
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: false }));
var risposta;
const cors = require('cors');
app.use(cors());


app.use(express.json());

app.get('/',(req,res) =>{
  const grafoattdiff = require('./grafoattdiff.json');
  res.json(grafoattdiff);
});


app.get('/passaggio-gen',(req,res)=>{
  const ls = spawn('python', ['genfrase.py']);
  ls.stdout.on('data', (data) => {
    console.log(`stdout: ${data.toString('utf-8')}`);
    res.send( data );
  });
  ls.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
})

app.post('/passaggio-trascr', (req, res) => {
  const transcription = req.body.parametro1;
  const colore = req.body.parametro2;
  const lingua =req.body.parametro3;
  var TOKEN='';
  console.log(lingua);
  if(lingua=='italiano'){
       TOKEN = 'UQWQ55BJSJ2HJ7KLVE72LRFSOBABHH4P';}
  else{ 
      TOKEN = '6FND2QRA2AQ2B45GHC3JV5MN5RYT2C5Y';}


  console.log('Recezione:', transcription, colore, lingua);
  fetch(`https://api.wit.ai/message?q=${encodeURIComponent( transcription)}`, {
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      'Content-Type': 'application/json',
    },
  })
    .then(response => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('Errore nella richiesta a Wit.ai');
    })
    .then(data => {
      if(data.intents[0]!=undefined){
      risposta = data.intents[0].id;
      console.log(risposta);
    fetch('http://localhost:4000/grafo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ transcription: risposta , colore: colore ,lingua: lingua})
    })
      .then(response => response.json())
      .then(data => {
        console.log('Trascrizione processata:', data);
        res.json({data});
      })
      .catch(error => {
        console.error('Errore:', error);
      });
      }else{

        res.json(
          {
            "data": {
              "message": "Non so darti una risposta"
            }
          });
      }

});
})
app.listen(port, () => {
  console.log(`Server in ascolto sulla porta ${port}`);
});
