// Write a code to convert days to years, months and days
// Notes: 1 year : 365 days, 1 month : 30 days

let totalDays = 400;

let year = Math.floor(totalDays / 365);
totalDays = totalDays % 365;

let month = Math.floor(totalDays / 30);
totalDays = totalDays % 30;

console.log(`
    ${year} year(s), ${month} month(s), ${totalDays} day(s)
`);