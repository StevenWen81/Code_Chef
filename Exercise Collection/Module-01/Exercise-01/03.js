// Write a code to find diameter, circumference and area 
// of a circle
// example: radius = 5
// output: diameter = 10, circumference = 31.4159, area = 78.539

const pi = Math.PI;
let radius = 5;

let diameter = 2 * radius;
let circumference = 2 * pi * radius;
let area = pi * radius * radius;

console.log(`
    diameter = ${diameter}, circumference = ${circumference}, area = ${area}
`);