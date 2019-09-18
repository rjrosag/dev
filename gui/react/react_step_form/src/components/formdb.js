var express = require('express');
var mysql = require('mysql');
var app  = express();

// Configuratgion DB
var connection = mysql.createConnection({
    host : 'localhost',
    user : 'me',
    password : 'secret', 
    database : 'my_db'
});

app.get('/'=>(req,res){
    connection.connect();
    connection.query('SELECT 1+1 AS solution', function(err, rows, fields) {
        if (err) throw err;
        console.log('The solution is: ', rows[0].solution);

        // Render Express View
        res.render('index':{'My Title', solution:rows[0].solution});
    });
    connection.end();
 })

 app.put('/'=>(req,res){
    connection.connect();
    connection.query('SELECT 1+1 AS solution', function(err, rows, fields) {
        if (err) throw err;
        console.log('The solution is: ', rows[0].solution);

        // Render Express View
        res.render('index':{'My Title', solution:rows[0].solution});
    });
    connection.end();
 })
