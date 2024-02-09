// Write a code that shows 1 if the input is a string, 2 if the input is a number,
// and 3 for others data type

let input = "hello";

if ( typeof(input) === "string" ) {
    console.log(1)
} else if ( typeof(input) === "number" ) {
    console.log(2)
} else {
    console.log(3)
}