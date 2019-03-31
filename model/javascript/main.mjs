function gameLogin(game, username, password) {
    if (game.players.length >= 50) {
        return false;
    } else if (game.players.length < 50 && !game.gameStart) {
        //check login
        //if login good, add player to game dict
        var newGuy = new Player("newbie");
        game.addPlayer(newGuy);
        return true;
    } else {
        console.log("Those credentials are incorrect!");
        return false;
    }
}

function gameLogout(game, playerModel) {
    game.removePlayer(playerModel)
}

function isWinner(game) {
    if (game.healthyPlayers <= 0) {
        game.infectedWin = true;
    } else if (game.healthyPlayers !== 0 && game.gameTime === 0) {
        game.playersWin = true;
        return game.players.keys
    } else {
        return false;
    }
}

const myMain = {'login': gameLogin, 'logout': gameLogout, 'winner': isWinner};
export default myMain;