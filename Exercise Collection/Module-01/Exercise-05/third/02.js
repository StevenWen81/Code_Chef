// Write a function from a given array of numbers and return the second
// smallest number

function getSecondSmallest ( arr ) {
    arr.sort((a,b) => a - b);

    return arr[1];
}

console.log(getSecondSmallest([5,3,1,7,2,6]))