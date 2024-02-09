// Create a function that can create a triangle pattern according
// to the height we provide like the following
// 01
// 02 03
// 04 05 06
// 07 08 09 10

function printNumber ( num ) {
    if ( num < 10 ) {
        return String("0" + num);
    } else {
        return String(num);
    }
}

function createPattern ( height ) {
    let col = 1;
    let currNumber = 1;

    for ( let i = 1; i <= height; i++ ) {
        let row = "";
        for ( let j = 0; j < col; j++ ) {
            row += printNumber(currNumber)
            if ( j+1 != col ) {
                row += " ";
            }
            currNumber += 1;
        }
        console.log(row);
        col += 1;
    }
}

createPattern(4);