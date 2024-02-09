// Write a function from the below array of number that will
// return sum of duplicate values

function sumOfDuplicate ( arr ) {
    let sumDuplicate = 0;

    let hash = {};

    for ( i of arr ) {
        if ( hash.hasOwnProperty(i) ) {
            hash[i] += 1;
        } else {
            hash[i] = 1;
        }
    }

    console.log(hash)

    for ( let key in hash ) {
        if ( hash[key] > 1) {
            sumDuplicate += key * hash[key];
        }
    }

    return sumDuplicate;
}

console.log(sumOfDuplicate([10, 20, 40, 10, 50, 30, 10, 60, 10]));