function checkForm() {
    // Get all the input elements in the form
    var inputs = document.querySelectorAll('input');
  
    // Loop through the input elements
    for (var i = 0; i < inputs.length; i++) {
      // If any of the input elements is empty, return false
      if (inputs[i].value == '') {
        return false;
      }
    }
  
    // If all input elements are filled out, return true
    return true;
}
var result = checkForm();
function signUpmsgi() {
    document.getElementById("alertsuccess").style.display= "block";
}
function validateMsg() {
    if (result){
        signUpmsgi()
    }
}