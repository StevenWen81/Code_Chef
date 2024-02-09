// Write a code to swap the case of each character from string

let input = "The QuiCk BrOwN Fox";

let swapCase = "";

for ( let i of input ) {
    if ( i == i.toUpperCase() ) {
        swapCase += i.toLowerCase();
    } else {
        swapCase += i.toUpperCase();
    }
}

console.log(swapCase);