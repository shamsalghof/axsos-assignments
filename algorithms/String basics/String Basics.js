// 1. Remove Blanks
function removeBlanks(str) {
  var newStr = "";
  for (let index = 0; index < str.length; index++) {
    if (str[index] === " ") {
      continue;
    }
    newStr += str[index];
  }
  return newStr;
}
var str = removeBlanks("shams sharief alghof");
console.log(str);

// 2. Get Digits
function getDigits(str) {
  var digit = "";
  for (let i = 0; i < str.length; i++) {
    if (isNaN(str[i])) {
      continue;
    }
    digit += str[i];
  }
  return digit;
}
console.log(getDigits("sg5kj89n3gfg"));

// 3. Acronyms
function acronym(str) {
  var arrStr = str.split(" ");
  var result = "";
  for (let i = 0; i < arrStr.length; i++) {
    result += arrStr[i][0];
  }
  return result.toUpperCase();
}
console.log(acronym("sha fdf fdg hh kfg fg"));

// 4. Count Non-Spaces
function countNonSpaces(str) {
  var num = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] !== " ") {
      num++;
    }
  }
  return num;
}
console.log(countNonSpaces("shand hamma var"));

// 5. Remove Shorter Strings
function removeShorterStrings(arr, minLength) {
  var arrShorterStrings = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].length >= minLength) {
        arrShorterStrings.push(arr[i]);
    }
    
  }
  return arrShorterStrings;
}
console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)); 
