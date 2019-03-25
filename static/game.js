function initGame() {
    var config = {
        type: Phaser.AUTO,
        width: window.innerWidth,
        height: window.innerHeight,
        scene: {
            preload: preload,
            create: create
        }
    };
    var game = new Phaser.Game(config);
    var human;
    var zombie;
    var background;
    var exitButton;
    preload();
    create();
    update();


    function preload() {
        this.load.image('background1', 'backgrounds\\background1.png');
        this.load.image('human', 'assets\\sprites\\human.png');
        this.load.image('zombie', 'assets\\sprites\\zombie.png');
        this.load.image('exitButton', 'assets\\ui\\ExitButton.png');  //TODO onclick send ajax request to server with {"game_id": game_id}
    }


    function create() {
        background = this.add.image(window.innerWidth / 2, window.innerHeight / 2, 'background1');
        background.setDisplaySize(window.innerWidth, window.innerHeight);
        human = this.add.sprite(window.innerWidth / 2, window.innerHeight / 2, 'human');
        zombie = this.add.sprite(window.innerWidth / 4, window.innerHeight / 2, 'zombie');
        exitButton = this.add.sprite(60, 50, 'exitButton');
        exitButton.setDisplaySize(window.innerWidth / 16, window.innerHeight / 10);
        human.angle = 270;
        zombie.angle = 270;
        exitButton.inputEnabled = true;
    }
}
