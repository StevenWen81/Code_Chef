// Write a code to format number as currency (IDR)
// eg. 1000 -> "Rp. 1.000,00"

// ------------------------
// test cases
// ------------------------
let input = 1000;
// let input = 15000;
// let input = 15000000;
// ------------------------

let strInput = String(input)
let length = strInput.length;

// logical reference
// 15000 -> 150-00 -> 15-000

// Count how many 3 consecutive number are there
let threeGroup = Math.floor(length / 3);

// Check is there is number left besides the threeGroup
let head;
if ( length % 3 == 0 ) {
    head = 3;
} else {
    head = length % 3;
}

let formated;

formated = strInput.slice(0, head)
if ( threeGroup > 0 ) {
    formated += ".";
}

for ( let i = 0; i < threeGroup; i++ ) {
    let start = head + (i * 3);
    let end = start + 3;
    formated += strInput.slice(start, end);
    if ( i < threeGroup - 1) {
        formated += ".";
    }
}

console.log("Rp. " + formated + ",00");