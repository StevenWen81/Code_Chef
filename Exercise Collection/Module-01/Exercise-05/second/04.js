// Write a function to find duplicate values in an array

function findDuplicate ( arr ) {
    let duplicated = [];

    arr.sort((a, b) => a - b);
    for ( let i = 0; i < arr.length; i++ ) {
        if ( arr[i] == arr[i-1] ) {
            if ( !duplicated.includes(arr[i]) ) {
                duplicated.push(arr[i]);
            }
        }
    }

    return duplicated;
}

console.log(findDuplicate([1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8]));