// =========================
// Always Hungry
// =========================

function alwaysHungry(arr) {

    var foundFood = false;

    for (var i = 0; i < arr.length; i++) {

        if (arr[i] === "food") {
            console.log("yummy");
            foundFood = true;
        }
    }

    if (foundFood === false) {
        console.log("I'm hungry");
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"]);
// yummy
// yummy

alwaysHungry([4, 1, 5, 7, 2]);
// I'm hungry



// =========================
// High Pass Filter
// =========================

function highPass(arr, cutoff) {

    var filteredArr = [];

    for (var i = 0; i < arr.length; i++) {

        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }

    return filteredArr;
}

var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);

console.log(result);
// [6, 8, 10, 9]



// =========================
// Better Than Average
// =========================

function betterThanAverage(arr) {

    var sum = 0;

    // Calculate total sum
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }

    // Calculate average
    var average = sum / arr.length;

    var count = 0;

    // Count numbers greater than average
    for (var i = 0; i < arr.length; i++) {

        if (arr[i] > average) {
            count++;
        }
    }

    return count;
}

var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);

console.log(result);
// 4



// =========================
// Array Reverse
// =========================

function reverse(arr) {

    var start = 0;
    var end = arr.length - 1;

    while (start < end) {

        // Swap values
        var temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }

    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);

console.log(result);
// ["e", "d", "c", "b", "a"]



// =========================
// Fibonacci Array
// =========================

function fibonacciArray(n) {

    // Starting values
    var fibArr = [0, 1];

    for (var i = 2; i < n; i++) {

        // Add last two numbers
        fibArr.push(fibArr[i - 1] + fibArr[i - 2]);
    }

    return fibArr;
}

var result = fibonacciArray(10);

console.log(result);
// [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]