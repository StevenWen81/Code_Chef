// Write a code to remove the first occurrence of a given "searh string"
// from a string
// eg. string = "Hello world", searh string = "ell" -> "Ho world"

// assumption: search string will always be a substring of the main string

let mainString = "Hello world";
let searchString = "ell";

let searchStringIndex = mainString.indexOf(searchString);
let endIndex = searchString.length + searchStringIndex;

let finalString = mainString.slice(0,searchStringIndex) + mainString.slice(4);
console.log(finalString)