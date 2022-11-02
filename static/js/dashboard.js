$('#id_first_name').prop("disabled", true);
$('#id_last_name').prop("disabled", true);
$('#id_email').prop("disabled", true);
$('#id_phone_number').prop("disabled", true);
document.getElementById('user-data-form').addEventListener("submit", submitForm)


function editUserData() {
    $('#id_first_name').prop("disabled", false);
    $('#id_last_name').prop("disabled", false);
    $('#id_phone_number').prop("disabled", false);
    $('#save-user-data').removeClass("disabled")
    $('#edit-user-data').addClass("disabled")
}

function submitForm() {
  $('#id_email').prop("disabled", false)
  console.log("worked") 
}

$("#alert-message").delay(4000).slideUp(400, function() {
  $(this).alert('close');
});