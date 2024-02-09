// Write a function to find the difference in 2 given array

function findDifference ( arr1, arr2 ) {
    let difference = [];

    for ( i of arr1 ) {
        if ( !arr2.includes(i) && !difference.includes(i)) {
            difference.push(i);
        }
    }

    for ( i of arr2 ) {
        if ( !arr1.includes(i) && !difference.includes(i)) {
            difference.push(i);
        }
    }

    return difference;
}

let a = [1,2,3,4,5];
let b = [3,4,5,6,7];

console.log(findDifference(a,b));