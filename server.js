import express from 'express'
const app=express()
app.listen(5001,()=>console.log('api running on port'))
app.get('/',(req,res)=>res.json('my Apifunziona'))