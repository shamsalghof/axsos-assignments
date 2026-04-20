function logout(element) {
  if (element.innerText === "logout") {
    element.innerText = "login";
  } else {
    element.innerText = "logout";
  }
}
function remove(element) {
    element.remove();
}
function likeAlert(element) {
    alert("Ninja was liked");
}