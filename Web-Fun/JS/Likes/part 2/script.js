// var likes = document.querySelector(".like");
// var num = parseInt(likes.innerText);
// function increment(params) {
//   num++;
//   likes.innerText = num + " ";
//   console.log(num);
// }

var spans = document.getElementsByClassName("like");//return html collection

var likesArr = []; //to store no of likes in each blog
for (var i = 0; i < spans.length; i++) {
  likesArr.push(parseInt(spans[i].innerText));
}

function addLikes(index) {
  likesArr[index]++;
  // console.log(likes[index]);
  var likeSpan = document.getElementsByClassName("like")[index];
  console.log(likeSpan);
  likeSpan.innerText = likesArr[index] +" ";
}
