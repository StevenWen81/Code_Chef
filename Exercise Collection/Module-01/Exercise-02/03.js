// Write a code to check whether the number is prime number
// or not
// eg. 7 -> is a prime number, 6 -> is not a prime number

// assumption: number will always be larger than 0

let number = 7;
let isPrimeStatement = `${number} is a prime number`;
let isNotPrimeStatement = `${number} is not a prime number`

if ( number == 1 ) {
    console.log(isNotPrimeStatement);
} else {
    let isPrime = true;
    for ( let i = 2; i <= Math.sqrt(number); i++ ) {
        if ( number % i == 0 ) {
            isPrime = false;
        }
    }

    ( isPrime ) ? console.log(isPrimeStatement) : console.log(isNotPrimeStatement);
}