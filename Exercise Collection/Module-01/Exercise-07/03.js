// Create a function to merge two array of student data and remove
// duplicate data. Student data contain name and email ( both string )

// assumption: inside of a single student data array, all is unique
function removeDuplicate ( arr1, arr2 ) {
    let merged = [...arr1];

    for ( let i of arr2 ) {
        let isUnique = true
        for ( let j of merged ) {
            if ( j.name === i.name && j.email === i.email ) {
                isUnique = false;
            }
        }

        if ( isUnique ) {
            merged.push(i);
        }
    }

    return merged;
}

let arr1 = [
    {name: "Student 1", email: "stud1@mail.com"},
    {name: "Student 2", email: "stud2@mail.com"},
];

let arr2 = [
    {name: "Student 1", email: "stud1@mail.com"},
    {name: "Student 3", email: "stud3@mail.com"},
];

console.log(removeDuplicate(arr1, arr2));