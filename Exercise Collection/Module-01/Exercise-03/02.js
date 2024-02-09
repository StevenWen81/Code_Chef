// Write a code to check whether a string is a palindrome or not
// eg. madam -> palindrome

let word = "madam";
let isPalindromeStatement = `${word} is a palindrome`;
let isNotPalindromeStatement = `${word} is not a palindrome`;

let left = 0;
let right = word.length - 1;

let isPalindrome = true;

while ( left < right ) {
    if ( word[left] != word[right] ) {
        isPalindrome = false;
    }
    left += 1;
    right -= 1;
}

isPalindrome ? console.log(isPalindromeStatement) : console.log(isNotPalindromeStatement);