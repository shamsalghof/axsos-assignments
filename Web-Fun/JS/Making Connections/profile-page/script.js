function changeName() {
  var name = document.querySelector("#name_jane");
  name.innerText = "shams alghof";
}

var requests = document.querySelector("#requests_id");
var connections = document.querySelector("#connection_id");
// function remove(element) {
//   //closest() = يطلع لفوق في الـ DOM لحد ما يلاقي .card-list-item
//   var card = element.closest(".card-list-item");
//   card.remove();
// }
console.log(connections.innerText );
function decline(element) {
  element.closest(".card-list-item").remove();
  --requests.innerText;
}

function accept(element) {
  element.closest(".card-list-item").remove();
  ++connections.innerText;
  --requests.innerText ;
}
