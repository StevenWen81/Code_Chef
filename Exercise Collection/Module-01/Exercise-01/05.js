// Write a code to get difference between dates in days.
// eg. date1 = 2022-01-20, date2 = 2022-01-22 -> 2

// assumption: 1 year has 365 days & 1 month has 30 days

let date1 = "2022-01-20";
let date1Day = Number(date1.slice(0,4)) * 365 + 
                Number(date1.slice(5,7)) * 30 +
                Number(date1.slice(8,10));

let date2 = "2022-01-22";
let date2Day = Number(date2.slice(0,4)) * 365 +
                Number(date2.slice(5,7)) * 30 +
                Number(date2.slice(8,10));

console.log(Math.abs(date1Day - date2Day))