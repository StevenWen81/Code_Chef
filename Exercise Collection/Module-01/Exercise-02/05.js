// Write a code to find factorial of a number
// eg. 4! = 24. 6! = 720

let number = 6;

let numberFactorial = 1;
for ( let i = 1; i <= number; i++ ) {
    numberFactorial *= i;
}

console.log(numberFactorial);