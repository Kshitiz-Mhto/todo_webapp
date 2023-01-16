var modal = document.getElementById('id01');
var modal1 = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
modal.style.display = "none";
}
}

window.onclick = function(event) {
  if (event.target == modal1) {
modal1.style.display = "none";
}
}

document.getElementById('detailform').addEventListener('submit', function(event) {
  event.preventDefault();
  var username = document.getElementById('usernamep').value;
  this.action = '/workspace/taskSaved/' + username
  this.submit();
});

// document.getElementById('editform').addEventListener('submit', function(event) {
//   event.preventDefault();
//   var title_id = document.getElementById('title_id').value;
//   this.action = '/workspaceTask/tasSaved/' + title_id
//   this.submit();
// });
