// Write a function that adds an element to the end of an array. However,
// the element should only be added if its not already in the array

function addUniqueElement ( arr, num ) {
    if ( !arr.includes(num) ) {
        arr.push(num);
    }

    return arr;
}

let arr = [1,2,3,4];
let newElement = 4;
console.log(addUniqueElement(arr, newElement));

newElement = 7;
console.log(addUniqueElement(arr, newElement));