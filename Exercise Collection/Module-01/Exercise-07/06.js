// Specifications
// Create a shooting game between two player
// Each player has three properties: name, health, and power
// Each player will take turn to shooting
// Before shooting, player get a chance to get random items ( health +10 or power +10)
// The game will continue until one of the player has health < 10

class ShootingGame {
    constructor ( player1, player2 ) {
        this.player1 = player1;
        this.player2 = player2;
    }

    getRandomItem() {
        let availableItems = [
            { health: 0 },
            { health: 10 },
            { power: 0 },
            { power: 10 },
        ]

        let randomIndex = Math.floor(Math.random() * availableItems.length);

        return availableItems[randomIndex];
    }

    start() {
        while ( true ) {
            console.log(`${this.player1.name} Turn`);
            this.player1.showStatus();
            this.player2.showStatus();
            console.log(`${this.player1.name} Consume and Shooting Phase`);
            this.player1.useItem(this.getRandomItem());
            this.player2.hit(this.player1.power);
            console.log(`${this.player1.name} Ending Phase`)
            this.player1.showStatus();
            this.player2.showStatus();
            if ( this.player2.health < 0 ) {
                console.log(`${this.player1.name} Win!!`);
                break;
            }

            console.log(`${this.player2.name} Turn`);
            this.player1.showStatus();
            this.player2.showStatus();
            console.log(`${this.player2.name} Consume and Shooting Phase`);
            this.player2.useItem(this.getRandomItem());
            this.player1.hit(this.player2.power);
            console.log(`${this.player2.name} Ending Phase`)
            this.player1.showStatus();
            this.player2.showStatus();
            if ( this.player1.health < 0 ) {
                console.log(`${this.player2.name} Win!!`);
                break;
            }
        }
       

    }
}

class Player {
    constructor ( name ) {
        this.name = name;
        this.health = 100;
        this.power = 10;
    }

    hit ( power ) {
        this.health -= power;
    }

    useItem ( item ) {
        for ( let key in item ) {
            if ( key == "health" ) {
                this.health += item[key];
            } else {
                this.power += item[key];
            }
        }
    }

    showStatus() {
        console.log(`
            ${this.name} ( Health => ${this.health}, Power => ${this.power} )
        `.trim());
    }
}

let player1 = new Player("P1");
let player2 = new Player("P2");

let game = new ShootingGame(player1, player2);

game.start();