class Player {
    name = "";
    health = 100;
    dead = false;
    gameId = 0;
    speed = 1;
    xPos = 0;
    yPos = 0;

    constructor(name) {
        this.name = name
    }

    respawn() {
        this.xPos = 0;
        this.yPos = 0;
        this.dead = false;
    }

    isDead() {
        if (this.health <= 0) {
            this.dead = true;
        }
    }

    gotHit(damage) {
        this.health -= damage;
        this.isDead();
        if (this.dead) {
            this.respawn()
        }
    }
}

class Game {
    players = {};
    infectedPlayers = 1;
    healthyPlayers = this.players.length - this.infectedPlayers;
    gameStart = false;
    infectedWin = false;
    playersWin = false;
    startTime = 0;
    currentTime = 0;
    displayTime = 0;
    lobbyTimer = 1;
    gameTimer = 1;
    gameTime = 300;

    stopGame() {
        if (this.infectedWin) {
            return "Infected win"
        } else {
            return "Players win"
        }
    }

    startGame() {
        this.gameStart = true;
        this.displayTime = 0;
        while (this.currentTime - this.startTime < this.gameTimer) {
            var replacement = Math.ceil(this.currentTime - this.startTime) - this.lobbyTimer
            if (replacement !== this.displayTime) {
                this.displayTime = replacement;
                this.gameTime -= 1;
            }
            this.currentTime = new Date().getTime()
        }
        this.stopGame()
    }

    startTimer() {
        while (this.currentTime - this.startTime < this.lobbyTimer) {
            if (Math.ceil(this.currentTime - this.startTime) !== this.displayTime) {
                this.displayTime = Math.ceil(this.currentTime - this.startTime)
            }
            this.currentTime = new Date().getTime()
        }
        this.startGame()
    }

    addPlayer(playerModel) {
        if (!this.players[playerModel.username]) {
            this.players[playerModel.username] = [playerModel.xPos, playerModel.yPos];
            return true;
        } else {
            return false;
        }
    }

    removePlayer(playerModel) {
        if (this.players[playerModel.username]) {
            delete this.players[playerModel.username];
            return true;
        } else {
            return false;
        }
    }

    constructor() {
        this.currentTime = new Date().getTime();
        this.startTime = new Date().getTime();
        this.startTimer()
    }
}

const myModule = {'player': Player, 'game': Game};
export default myModule;