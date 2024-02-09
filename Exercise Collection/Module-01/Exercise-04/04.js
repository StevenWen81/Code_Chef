// Write a function to remove all odd numbers in an array and return a new array
// that contains even numbers only

function filterEven ( arr ) {
    let evenArr = [];
    for ( i of arr ) {
        if ( i % 2 == 0 ) {
            evenArr.push(i);
        }
    }
    return evenArr
}

let arr = [1,2,3,4,5,6,7,8,9,10];
console.log(filterEven(arr));
