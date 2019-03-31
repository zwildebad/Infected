var mysql = require('mysql');

var con  = mysql.createConnection({
    host: 'localhost'
});

con.connect(function(err){
    if (err) throw err;
    console.log("Connected!");
    con.query(
        "CREATE DATABASE infected",
        function(err){
            if (err) throw err;
            console.log("Database created!");
        }
    );
});