/*
Question:
In this simple assignment you are given a number and 
have to make it negative. But maybe the number is 
already negative?

Notes:
1. The number can be negative already, in which case 
no change is required
2. Zero (0) is not checked for any specific sign. Negative 
zeros make no mathematical sense

Sample Test Case
makeNegative(1)    // return -1
makeNegative(-5)   // return -5
makeNegative(0)    // return 0
makeNegative(0.12) // return -0.12
*/

function makeNegative(float $num) : float
{
    return ($num > 0 ? (-1 * $num) : $num);
}