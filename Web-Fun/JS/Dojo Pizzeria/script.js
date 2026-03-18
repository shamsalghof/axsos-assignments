var sandwich = {
  bread: "sourdough",
  protein: "london broil",
  cheese: "lacey swiss cheese",
  toppings: ["romaine lettuce", "heirloom tomatoes", "horseradish sauce"],
};

console.log(sandwich);
function sandwichFactory(bread, protein, cheese, toppings) {
  var sandwich = {};
  sandwich.bread = bread;
  sandwich.protein = protein;
  sandwich.cheese = cheese;
  sandwich.toppings = toppings;
  return sandwich;
}

var s1 = sandwichFactory("wheat", "turkey", "provolone", [
  "mustard",
  "fried onions",
  "arugula",
]);
console.log(s1);
//the solution
function pizzaOven(crust, sauce, cheeses, toppings) {
  var pizza = {};
  pizza.crust = crust;
  pizza.sauce = sauce;
  pizza.cheeses = cheeses;
  pizza.toppings = toppings;
  return pizza;
}

// Create a pizza with: , , , and
// Create a pizza with: "hand tossed", "marinara", ["mozzarella", "feta"], and ["mushrooms", "olives", "onions"]
var pizza1 = pizzaOven(
  "deep dish",
  "traditional",
  ["mozzarella"],
  ["pepperoni", "sausage"],
);
var pizza2 = pizzaOven(
  "hand tossed",
  "marinara",
  ["mozzarella", "feta"],
  ["mushrooms", "olives", "onions"],
);

var pizza3 = pizzaOven(
  "deep dish",
  "traditional",
  ["mozzarella"],
  ["Green Olives", "mayoniz"],
);
var pizza4 = pizzaOven(
  "hand tossed",
  "marinara",
  ["mozzarella", "feta"],
  ["Katchup", "Tomato"],
);

// crust, sauce, cheeses, toppings
crusts = ["Thin crust", "Thick crust", "Deep Dish", "hand tossed"];
sauces = ["traditional", "marinara", "Katchep", "pestashio"];
cheeses = [["mozzarella"], ["mozzarella", "feta"], "k"];
toppings = [
  ["Green Olives", "mayoniz"],
  ["mushrooms", "olives", "onions"],
];
//Bounes
function randomPizza() {
  let randomCrust = crusts[Math.floor(Math.random() * crusts.length)];
  let randomSauce = sauces[Math.floor(Math.random() * sauces.length)];
  let randomCheese = cheeses[Math.floor(Math.random() * cheeses.length)];
  let randomTopping = toppings[Math.floor(Math.random() * toppings.length)];

  return pizzaOven(randomCrust, randomSauce, [randomCheese], [randomTopping]);
}

console.log(randomPizza());
console.log(randomPizza());
