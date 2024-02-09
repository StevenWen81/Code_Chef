// Write a function to get the lowest, highest and average value in
// the array ( with and without sort function )

// assumption: arr will always have at least one element inside of it.

function solve ( arr ) {
    let low = arr[0];
    let high = arr[0];
    let total = 0;

    for ( i of arr ) {
        if ( i < low ) {
            low = i;
        }
        if ( i > high ) {
            high = i;
        }

        total += i;
    }

    let avg = Number((total / arr.length).toFixed(4));

    let value = {
        lowest: low,
        highest: high,
        average: avg
    }

    return value;
}

function solveSort ( arr ) {
    arr.sort((a, b) => a - b);

    let sum = 0;
    for ( i of arr ) {
        sum += i;
    }

    let avg = Number((sum / arr.length).toFixed(4))

    value = {
        lowest: arr[0],
        highest: arr[arr.length - 1],
        average: avg
    }

    return value;
}

console.log(solve([12,5,23,18,4,45,32]));
console.log(solveSort([12,5,23,18,4,45,32]));