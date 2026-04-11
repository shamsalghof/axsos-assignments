function showAlert(cityName) {
  alert("welcome to city " + cityName);
}

function acceptCookies() {
  let cookieBox = document.getElementById("cookieBox");
  cookieBox.remove();
}

document.getElementById("tempUnit").addEventListener("change", (event) => {
  console.log("Selected value:", event.target.value);
  let temps = document.querySelectorAll(".temp");

  if (event.target.value == "f") {
    for (var i = 0; i < temps.length; i++) {
       let cTemp = parseInt(temps[i].innerText);
      temps[i].innerText = cToF(cTemp) + "°";
    }
  } else {
    for (var i = 0; i < temps.length; i++) {
     let fTemp = parseInt(temps[i].innerText);
      temps[i].innerText = fToC(fTemp) + "°";
    }
  }
});

function cToF(celsius) {
  return Math.ceil((celsius * 9) / 5 + 32);
}
function fToC(fahrenheit) {
  return  Math.ceil(((fahrenheit - 32) * 5) / 9);
}
