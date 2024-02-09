// Write a code to change every letter a into * from a string of input

let input = "An apple a day keeps the doctor away";

let starredInput = "";

for ( let i = 0; i < input.length; i++ ) {
    if ( input[i] == 'a' || input[i] == 'A') {
        starredInput += "*"
    } else {
        starredInput += input[i]
    }
}

console.log(starredInput);