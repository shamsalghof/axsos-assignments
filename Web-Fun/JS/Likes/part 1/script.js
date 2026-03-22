var likes = document.querySelector(".like");
var num = parseInt(likes.innerText);
function increment(params) {
  num++;
  likes.innerText = num + " ";
  console.log(num);
}

