$('#id_first_name').prop("disabled", true);
$('#id_last_name').prop("disabled", true);
$('#id_email').prop("disabled", true);
$('#id_phone_number').prop("disabled", true);
document.getElementById('user-data-form').addEventListener("submit", submitForm);
let cancelButtons = document.getElementsByClassName('cancelButton');
Array.from(cancelButtons).forEach(function(cancelButtons) {
  cancelButtons.addEventListener('click', listenToCancel);
});

function editUserData() {
    $('#id_first_name').prop("disabled", false);
    $('#id_last_name').prop("disabled", false);
    $('#id_phone_number').prop("disabled", false);
    $('#save-user-data').removeClass("disabled")
    $('#edit-user-data').addClass("disabled")
}

function submitForm() {
  $('#id_email').prop("disabled", false)
}

let id = ""

function listenToCancel(e) {
  id = e.target.value
  let new_id = `cancel-appointment-${id}`
  $('#cancel-appointment').attr("id", new_id)
  document.getElementById(new_id).addEventListener("click", cancelAppointment);
}

function cancelAppointment() {
  document.getElementById(id).submit()
}

$("#alert-message").delay(4000).slideUp(400, function() {
  $(this).alert('close');
});