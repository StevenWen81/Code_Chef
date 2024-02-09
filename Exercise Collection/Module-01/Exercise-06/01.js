// Create a function to calculate array of student data
// student data contains name (string), email (string), 
// age (date), and score (number)
// return values (object)
// score -> highest, lowest, average
// age -> highest, lowest, average

function calculateStudentData ( studentsData ) {
    let highestScore;
    let lowestScore;
    let averageScore = 0;
    let highestAge;
    let lowestAge;
    let averageAge = 0;

    
    for ( i of studentsData ) {
        // Score Data Processing Part
        averageScore += i.Score;
        if ( highestScore == undefined && lowestScore == undefined) {
            highestScore = i.Score;
            lowestScore = i.Score;
        }

        if ( i.Score > highestScore ) {
            highestScore = i.Score;
        }

        if ( i.Score < lowestScore) {
            lowestScore = i.Score;
        }
        
        // Age Data Processing Part
        const currentYear = new Date().getFullYear(); // 2024
        const studentBornYear = new Date(i.Age).getFullYear();
        let studentAge = currentYear - studentBornYear;

        averageAge += studentAge;

        if ( highestAge == undefined && lowestAge == undefined ) {
            highestAge = studentAge;
            lowestAge = studentAge;
        }

        if ( studentAge > highestAge ) {
            highestAge = studentAge;
        }

        if ( studentAge < lowestAge ) {
            lowestAge = studentAge;
        }
    }

    averageScore = Number((averageScore / studentsData.length).toFixed(2));

    averageAge = Number((averageAge / studentsData.length).toFixed(0)); 

    let values = {
        Score: {
            Highest: highestScore,
            Lowest: lowestScore,
            Average: averageScore,
        },
        Age: {
            Highest: highestAge,
            Lowest: lowestAge,
            Average: averageAge,
        }
    }

    return values;
}

studentArray = [
    {Name: "John", Email: "John@test.com", Age: new Date("2000-01-01"), Score: 80},
    {Name: "Jane", Email: "Jane@test.com", Age: new Date("2000-10-01"), Score: 95},
    {Name: "Juan", Email: "Juan@test.com", Age: new Date("2010-01-01"), Score: 72},
];

console.log(calculateStudentData(studentArray));
