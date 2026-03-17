var myVideo = document.getElementById("myVideo");

// function over(param) {
//   myVideo.play();
// }
// function out(param) {
//   myVideo.pause();
// }
myVideo.addEventListener("mouseover", function () {
  this.play();
});
myVideo.addEventListener("mouseout", function () {
  this.pause();
});
