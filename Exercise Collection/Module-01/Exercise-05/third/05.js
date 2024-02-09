// Write a game of rock, paper, scissor function that will return "Win" of "Lose"
// The function will randomly pick between rock, paper, or scissor.

function play ( selection ) {
    let bot = randomSelection();

    return decision(selection, bot);
}

function randomSelection() {
    let availableMove = ["rock", "paper", "scissor"];

    let randomMove = Math.floor(Math.random() * availableMove.length);

    return availableMove[randomMove];
}

function decision ( selection, bot ) {
    let winMsg = `You use ${selection} and Bot use ${bot}, You Win!!`
    let loseMsg = `You use ${selection} and Bot use ${bot}, You Lose :(`
    let drawMsg = `You use ${selection} and Bot use ${bot}, It's a Draw!`

    if ( selection == bot ) {
        return drawMsg;
    } else if ( selection == "rock" && bot == "scissor" ||
            selection == "paper" && bot == "rock" ||
            selection == "scissor" && bot == "paper") {
        return winMsg;
    } else {
        return loseMsg;
    } 
}

console.log(play("rock"));
