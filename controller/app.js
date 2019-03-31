var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var main = require('model/javascript/main');
var classes = require('model/javascript/gameClasses');

app.use(express.static('C:\\Users\\Alex\\IdeaProjects\\Infected\\controller\\public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function(req, res){
    res.sendFile('C:\\Users\\Alex\\IdeaProjects\\Infected\\controller\\views\\index.html');
});

app.post('/login', function(req, res) {
    var username = req.body['username'];
    var password = req.body['password'];
    var newUser = req.body['new_user'];
    //if username and password check out redirect to game
    res.redirect('/game')
});

app.get('/game', function(req, res){
    res.sendFile('C:\\Users\\Alex\\IdeaProjects\\Infected\\controller\\views\\game.html');
});

app.get('/game/background1.png', function(req, res){
    res.sendFile('C:\\Users\\Alex\\IdeaProjects\\Infected\\controller\\public\\assets\\backgrounds\\background1.png');
});

app.get('/game/human.png', function(req, res){
    res.sendFile('C:\\Users\\Alex\\IdeaProjects\\Infected\\controller\\public\\assets\\sprites\\human.png');
});

app.get('/game/zombie.png', function(req, res){
    res.sendFile('C:\\Users\\Alex\\IdeaProjects\\Infected\\controller\\public\\assets\\sprites\\zombie.png');
});

app.get('/game/ExitButton.png', function(req, res){
    res.sendFile('C:\\Users\\Alex\\IdeaProjects\\Infected\\controller\\public\\assets\\ui\\ExitButton.png');
});

const g = new classes.game();
const newbie = new classes.player('newbie');
console.log(main.login(g, 'newbie', 'pass'));
app.listen(3000, console.log("Listening on 3000"));