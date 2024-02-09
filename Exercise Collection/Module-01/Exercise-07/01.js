// Create a function to check if two objects are equal

function isObjectEqual ( obj1, obj2 ) {
    const keyObj1 = Object.keys(obj1);
    const keyObj2 = Object.keys(obj2);

    console.log(keyObj1);
    console.log(keyObj2);
    if ( keyObj1.length != keyObj2.length ) {
        return false;
    }

    for ( let key in obj1 ) {
        if ( obj1[key] !== obj2[key] ) {
            return false;
        }
    }

    return true;
}

let o1 = { a: 2 };
let o2 = { a: 1 };
console.log(isObjectEqual(o1, o2));

o1 = { a: "Hello" };
o2 = { a: 1 };
console.log(isObjectEqual(o1, o2));

o1 = { a: 1 };
o2 = { a: 1 };
console.log(isObjectEqual(o1, o2));