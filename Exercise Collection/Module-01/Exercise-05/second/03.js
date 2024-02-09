// Write a function that will combine 2 given array into one array

function combineTwoArr ( arr1, arr2 ) {
    return [...arr1, ...arr2];
}

let a = [1,2,3];
let b = [1,2,3];

console.log(combineTwoArr(a,b));