// Write a code to print the first N fibonacci numbers

let a = 1;
let b = 1;

let n = 15;
if ( n < 3 ) {
    console.log(1);
} else {
    for ( let i = 0; i < n-2; i++ ) {
        c = a + b;
        a = b;
        b = c;
    }

    console.log(b); 
}
