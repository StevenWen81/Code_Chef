// Create a function that can accept input as an array of object
// and switch all values into property and propert into value

function switchKeyValue ( arrOfOjb ) {
    let switched = [];

    for ( let i of arrOfOjb ) {
        let tempObj = {};
        for ( let key in i ) {
            tempObj[i[key]] = key;

        }
        switched.push(tempObj);
    }

    return switched;
}

let arr1 = [
    { name: "David", age: 20 },
];
console.log(switchKeyValue(arr1));

let arr2 = [
    { name: "Test", age: 40 },
    { name: "Test2", age: 30 },
];
console.log(switchKeyValue(arr2));