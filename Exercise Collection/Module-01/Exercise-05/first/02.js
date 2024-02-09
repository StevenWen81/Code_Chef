// Write a function that takes an array of words and returns a string
// by concatenating the words in the array, seperated by commas and
// the last word by an "and".

function stringifyArray ( arr ) {
    let strArr = "";

    for ( let i = 0; i < arr.length; i++ ) {
        if ( i + 1 != arr.length ) {
            strArr += arr[i];
            strArr += ", ";
        } else {
            strArr += "and ";
            strArr += arr[i];
        }
    }

    return strArr;
}

console.log(stringifyArray(["apple", "banana", "cherry", "date"]));