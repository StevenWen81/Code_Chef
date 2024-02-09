// Bases on the array below write a function that will return
// primitive data types only.

function filterPrimitive ( arr ) {
    let primitive = [];

    for ( i of arr ) {
        if ( typeof(i) !== 'object' || i == null) {
            primitive.push(i);
        }
    }

    return primitive;
}

console.log(filterPrimitive([1, [], undefined, {}, "string", {}, []]));