// Write a function to insert multiple given integer ( not an array ) to
// an array and have a maximum size input. the array can only have a maximum
// size from a given input.

function limitedArray( limit, ...nums ) {
    return nums.slice(0,limit); 
}

let maxSize = 5;

console.log(limitedArray(maxSize, 5, 10, 24, 3, 6, 7, 8));