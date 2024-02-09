// Write a function to calculate each element in the same position
// fromm two arrays of integer. Assume both arrays are of the same
// length

function sumTwoArrays ( arr1, arr2 ) {
    let finalArr = [];

    for ( let i = 0; i < arr1.length; i++ ) {
        let sumElement = arr1[i] + arr2[i];

        finalArr.push(sumElement);
    }

    return finalArr;
}

let a = [1,2,3];
let b = [3,2,1];

console.log(sumTwoArrays(a,b));