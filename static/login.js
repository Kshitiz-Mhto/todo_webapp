document.getElementById('loginform').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    this.action = '/workspace/' + username;
    this.submit();
  });
  