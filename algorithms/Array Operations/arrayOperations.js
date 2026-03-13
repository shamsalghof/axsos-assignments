//1. Accessing Elements
let colors = ["red", "blue", "green", "yellow", "purple"];
console.log(colors[0]); //first element
console.log(colors[colors.length - 1]); // last element
console.log(colors[1]); //second element
colors[2] = "orange"; // update third element
console.log(colors); // print updated array
console.log("----------------------------------------");
// 2. Traversing an Array
let numbers = [10, 20, 30, 40, 50];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]); // print array
}
for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]); // print inverse array
}
console.log("------------------------------------------");
//3.  Searching in an Array
let number = [5, 10, 15, 20, 25];
if (number.indexOf(25) != -1) {
  console.log("Found at position " + number.indexOf(25));
} else {
  console.log("Not Found");
}
console.log("------------------------------------------");
// 4. Sorting an Array
let scores = [50, 20, 70, 10, 40];
scores.sort((a, b) => a - b); // sorting asccending
console.log(scores);
scores.sort((a, b) => b - a); // sorting descending
console.log(scores);
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
console.log(names.sort()); // sorting alphapitical order
console.log("----------------------------------------------");
// 5.  Inserting Elements
let animals = ["dog", "cat", "rabbit"];
animals.push("elephant"); // Add "elephant" to the end of the array.
console.log(animals);
animals.unshift("lion"); //Add "lion" to the beginning of the array.
console.log(animals);
animals.splice(2, 0, "tiger"); // Insert "tiger" between "dog" and "cat".
console.log(animals);
console.log("------------------------------------------");
// 6. Deleting Elements
let fruits = ["apple", "banana", "cherry", "date"];
fruits.shift(); // remove first element
console.log(fruits);
fruits.pop(); // remove last element
console.log(fruits);
fruits.splice(fruits.indexOf("banana"), 1); // Remove "banana" from the array without using its index directly.
console.log(fruits);
console.log("------------------------------------------");
//7. Combining Arrays
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
combinedArray = array1.concat(array2);
console.log(combinedArray);
console.log("------------------------------------------");
//8. Splitting an Array
let items = ["a", "b", "c", "d", "e"];
let arr1 = items.slice(0, 3);
let arr2 = items.slice(3, 5);
console.log(arr1);
console.log(arr2);
console.log("------------------------------------------------");
// 9. Filtering Elements
let nums = [1, 5, 10, 15, 20, 25, 30];
let filteredArray = nums.filter((num) => num > 15); //Create a new array containing only numbers greater than 15.
console.log(filteredArray);
console.log("----------------------------------------------------------------");
//10.  Advanced Challenge
let duplicate = [1, 2, 2, 3, 4, 4, 5];
let unique = [...new Set(duplicate)];
console.log(unique);
console.log("----------------------------------------------------------------");

//Bonus Challenge
let input1 = [7, 10, 2];
let input2 = [1, 0, 3];
//[7, 10, 2,11,20,14,16,13] // i = 0
//inside for: [7, 2, 10,11,20,14,16,13] condition not met
//inside for: [7, 2, 10,11,20,14,16,13] condition not met
//[7, 2, 10,11,14,20,16,13] --> swap 20, 14
//[7, 2, 10,11,14,16,20,13] --> swap 20, 16
//[7, 2, 10,11,14,16,13,20] --> swap 20, 13
//outer loop second iteration i = 1
//[2, 7, 10,11,14,16,13,20] swap 7,2
//[2, 7, 10,11,14,16,13,20] cndition not met
//[2, 7, 10,11,14,16,13,20] cndition not met
//[2, 7, 10,11,14,16,13,20] cndition not met
//[2, 7, 10,11,14,16,13,20] cndition not met
//[2, 7, 10,11,14,13,16,20] swap 13,16
function bubbleSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

bubbleSort(input1);
bubbleSort(input2);
for (var i = 0; i < input2.length; i++) {
  input1.push(input2[i]);
}
bubbleSort(input1);
console.log(input1);
