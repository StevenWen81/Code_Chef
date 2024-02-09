// Write a code to display the multiplication table of a
// given integer

let number = 9;

for ( let i = 1; i <= 10; i++ ) {
    let multiplicationResult = i * number;

    console.log(`
        ${number} x ${i} = ${multiplicationResult}
    `);
}