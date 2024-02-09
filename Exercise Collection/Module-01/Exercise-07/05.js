// Create a function to find a factorial number using recurrsion

function countFactorial ( num ) {
    // base
    if ( num == 1 ) {
        return 1
    } else { // recurrence
        return num * countFactorial(num - 1)
    }
}

console.log(countFactorial(5));