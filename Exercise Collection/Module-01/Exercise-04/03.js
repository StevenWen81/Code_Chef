// Create a function to calculate Body Mass Index (BMI)
// Formula: BMI = weight / height^2

function calculateBMI ( weight, height ) {
    let heightSquare = height * height;
    let bmi = Number((weight / heightSquare).toFixed(1)); // Note that .toFixed return a string

    if ( bmi < 18.5 ) {
        return "less weight";
    } else if ( 18.5 <= bmi && bmi <= 24.9 ) {
        return "ideal";
    } else if ( 25.0 <= bmi && bmi <= 29.9 ) {
        return "overweight";
    } else if ( 30.0 <= bmi && bmi <= 39.9 ) {
        return "very overweight";
    } else {
        return "obesity";
    }
}

console.log(calculateBMI(70, 1.7));

