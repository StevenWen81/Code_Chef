// Write a conditional statement to sort three numbers
// eg. num1 = 42, num2 = 27, num3 = 18 -> 18, 27, 42

let num1 = 42;
let num2 = 27;
let num3 = 18;

let biggest = Math.max(Math.max(num1, num2), num3);
let smallest = Math.min(Math.min(num1, num2), num3);

let middle = num1 + num2 + num3 - biggest - smallest;

console.log(smallest + ", " + middle + ", " + biggest)

// 3 2 1 -> 2 3 1 -> 2 1 3 -> 1 2 3
// 2 3 1 -> 2 3 1 -> 2 1 3 -> 1 2 3
// 3 1 2 -> 1 3 2 -> 1 2 3 -> 1 2 3
// 3x rotate will guarantee to fix the order

num1 = 42;
num2 = 27;
num3 = 18;

if ( num1 > num2 ) {
    let temp = num1;
    num1 = num2;
    num2 = temp;
}

if ( num2 > num3 ) {
    let temp = num2;
    num2 = num3;
    num3 = temp;
}

if ( num1 > num2 ) {
    let temp = num1;
    num1 = num2;
    num2 = temp;
}

console.log(num1 + ", " + num2 + ", " + num3)