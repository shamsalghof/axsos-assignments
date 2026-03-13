function convertToCelsius(fahrenheitTemp) {
  var celsiusTemp = ((fahrenheitTemp - 32) * 5) / 9;
  return "the Tempreture in Celsius is " + celsiusTemp;
}
var Tempreture = convertToCelsius(40);
console.log(Tempreture);
