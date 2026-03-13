// 1- print numbers from 1 to 10
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
console.log("-----------------------------");

// 2- Reverse Counting
for (let i = 10; i >= 0; i--) {
  console.log(i);
}
console.log("-----------------------------");

// 3- Even Numbers
for (let i = 1; i <= 20; i++) {
  if (i % 2 === 0) {
    console.log(i);
  }
}
console.log("-----------------------------");

// 4- Odd Numbers
for (let i = 1; i <= 20; i++) {
  if (i % 2 != 0) {
    console.log(i);
  }
}
console.log("-----------------------------");

// 5- Sum of Numbers
var sum = 0;
for (let i = 1; i <= 10; i++) {
  sum += i;
}
console.log(sum);
console.log("-----------------------------");

// 6- FizzBuzz
for (let i = 1; i <= 30; i++) {
  if (i % 5 === 0 && i % 3 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  }
}
console.log("-----------------------------");
