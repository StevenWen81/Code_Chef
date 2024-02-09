// Create a function to get the intersect of two objects

function getIntersect ( obj1, obj2 ) {
    let merged = {};

    for ( let key in obj1 ) {
        // Check to find intersect key
        if ( obj2.hasOwnProperty(key) ) {
            // Check for intersect key and also the value
            if ( obj1[key] === obj2[key] ) {
                merged[key] = obj1[key];
            }
        }
    }

    return merged;
}

let o1 = { a: 1, b: 2 };
let o2 = { a: 1, c: 3 };
console.log(getIntersect(o1, o2));