// Create a function that can loop the number of times according
// to the input we provide, and will replace multiples of 3 with
// "Fizz", multiples of 5 with "Buzz", multiples of 3 and 5 with 
// "FizzBuzz".

function fizzBuzzSequence ( num ) {
    let fbSequence = "";

    for ( let i = 1; i <= num; i++ ) {
        if ( i % 3 == 0 && i % 5 == 0) {
            fbSequence += "FizzBuzz";
        } else if ( i % 3 == 0 ) {
            fbSequence += "Fizz";
        } else if ( i % 5 == 0 ) {
            fbSequence += "Buzz";
        } else {
            fbSequence += String(i);
        }

        if ( i != num) {
            fbSequence += " ";
        }
    }

    return fbSequence;
}

console.log(fizzBuzzSequence(6));