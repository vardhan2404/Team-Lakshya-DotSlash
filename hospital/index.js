const app = require('express')()
const path = require('path')
const MongoClient = require('mongodb').MongoClient

const fs = require('fs');
const cheerio = require('cheerio');

const html = fs.readFileSync('C:/Users/kvard/OneDrive/Desktop/hospital/home.html', 'utf8');
const $ = cheerio.load(html);
const h1Value = $('h1').text();


var url = 'mongodb://localhost:27017/';

app.get('/',(req, res)=>{
    res.sendFile(path.join(__dirname,'/home.html'))
})

app.post('/action', (req,res)=>{
    const fs = require('fs');
    const cheerio = require('cheerio');

    const html = fs.readFileSync('C:/Users/kvard/OneDrive/Desktop/hospital/home.html', 'utf8');
    const $ = cheerio.load(html);
    const h1Value = $('#counter').text();

    const doc = { title: h1Value };

    MongoClient.connect(url, function(err,db){
        if(err) throw err;
        var dbo = db.db("hms")
        dbo.collection("bms").insertOne(doc, function(err,res){
            if(err) throw err;
            console.log("inserted")
            db.close()
        })
            
    })

});


app.listen(8080)