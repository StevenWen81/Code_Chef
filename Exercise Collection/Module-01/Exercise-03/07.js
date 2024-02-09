// Write a code to reverse a string
// eg. hello -> olleh

let input = "hello"
let reversedInput = ""

for ( let i = 0; i < input.length; i++ ) {
    reversedInput = input[i] + reversedInput;
}

console.log(reversedInput)