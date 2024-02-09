// Write a function from given array of mixed data types and return the sum
// of all the number

function sumNumber ( arr ) {
    let ans = 0;
    for ( i of arr ) {
        if ( typeof(i) == 'number' ) {
            ans += i
        }
    }

    return ans;
}

console.log(sumNumber(["3", 1, "string", null, false, undefined, 2]));