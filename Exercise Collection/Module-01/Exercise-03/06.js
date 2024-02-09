// Write a code to capitalize the first letter of each  word in a string
// eg. "hello world" -> "Hello World"

let input = "hello world";

let arrInput = input.split(" ");

for ( let i = 0; i < arrInput.length; i++ ) {
    arrInput[i] = arrInput[i][0].toUpperCase() + arrInput[i].slice(1);
}

let capsWord = arrInput.join(" ");

console.log(capsWord);