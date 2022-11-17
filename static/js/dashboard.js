// script for handling user edit form in dashboard.

// make all fields disabled on first load.
$('#id_first_name').prop("disabled", true);
$('#id_last_name').prop("disabled", true);
$('#id_email').prop("disabled", true);
$('#id_phone_number').prop("disabled", true);


// add eventlistener to submit button, which calls submitForm function.
document.getElementById('user-data-form').addEventListener("submit", submitForm);

// add eventlistener to cancelButton on Modal.
let cancelButtons = document.getElementsByClassName('cancelButton');
Array.from(cancelButtons).forEach(function(cancelButtons) {
  cancelButtons.addEventListener('click', listenToCancel);
});

function editUserData() {
  // makes user data fields enabled, called when Edit button is clicked (see html).
    $('#id_first_name').prop("disabled", false);
    $('#id_last_name').prop("disabled", false);
    $('#id_phone_number').prop("disabled", false);
    $('#save-user-data').removeClass("disabled");
    $('#edit-user-data').addClass("disabled");
}

function submitForm() {
  // makes email field enabled right before sending data to backend.
  $('#id_email').prop("disabled", false);
}

let id = "";

function listenToCancel(e) {
  // listens to modal cancel button, passes Id of appointment.
  id = e.target.value;
  let new_id = `cancel-appointment-${id}`;
  $('#cancel-appointment').attr("id", new_id);
  document.getElementById(new_id).addEventListener("click", cancelAppointment);
}

function cancelAppointment() {
  // submits form to cancel appointment.
  document.getElementById(id).submit();
}

$("#alert-message").delay(4000).slideUp(400, function() {
  // slide up for alert message (when user data is edited) after 4 seconds.
  $(this).alert('close');
});