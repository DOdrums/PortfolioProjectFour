var disabledWeekDays = planningJS.disabled_weekdays.split(",")
var disabledWeekDaysList = disabledWeekDays.map(function (x) {
  return parseInt(x, 10)
})


dateToday = new Date()
var allowTimesFinal = planningJS.allow_times.split(",")
// get allowedTimes entered in admin panel by site owner
getBlockedTimesList(dateToday)
// get allowedTimes with currently booked appointments blocking times.
// this is done per day, so the list changes when a new date is selected.
var selectedTreatmentDuration = 180

document.getElementById('id_treatment_name').addEventListener('change', setTreatment, true);
// get value from selected treatment option and store duration value in selectedTreatmentDuration
function setTreatment(e) {
  selectedTreatmentDuration = parseInt(e.target.value.split(",")[1])
  console.log(selectedTreatmentDuration)
}

function getAllowdTimesListWithDate(date) {
  // get allowed times with date appended, for comparing times
  let allowedTimesList = []
  let timeoption = date.split("T").shift()
  timelist = planningJS.allow_times.split(",")
  for (time of timelist) {
  timeDate = timeoption + "T" + time
  timeDate = new Date(timeDate)
  allowedTimesList.push(timeDate)
  }
  return allowedTimesList
}

function getBlockedTimesList(selectedDate) {
  // compares times in allowedTimes with appointments. Block out any
  // times that appointments are scheduled. Also checks for selected treatments
  // duration, making sure the appointment can't be scheduled with an end time
  // later than the registered endtime by sitowner.
  let allowedTimesList = getAllowdTimesListWithDate(selectedDate.toISOString())

  appointments.forEach(element => {
    appDate = new Date(element.date_time)

    if (appDate.toDateString() === selectedDate.toDateString()) {
      let startTime = appDate
      let endTime = new Date(appDate.getTime() + element.duration*60000)
      for (time of allowedTimesList) {
        if (startTime <= time && time < endTime) {
          allowedTimesList = allowedTimesList.filter(e => e !== time);
        }
      }
    }
  });
  let blockedTimesList = allowedTimesList
  convertBlockedTimesList(blockedTimesList)
}

function convertBlockedTimesList(blockedTimesList) {
  // convert allowedTimesList back to the format for
  // usage in datepicker.
  allowTimesFinal.length = 0
    for (dateTime of blockedTimesList) {
      let time = dateTime.getHours() + ":" + dateTime.getMinutes();
      allowTimesFinal.push(time)
    }
}

jQuery('#datepicker').datetimepicker({
  format:'c',
  inline:true,
  lang:'en',
  todayButton:true,
  allowTimes: allowTimesFinal,
  disabledWeekDays: disabledWeekDaysList,
  disabledDates: planningJS.disabled_dates.split(","), formatDate: 'd.m.Y',
  onChangeDateTime: function(dp, $input) {
    let selectedDate = new Date($input.val())
    getBlockedTimesList(selectedDate)
    $('#datepicker').datetimepicker('setOptions', {allowTimes: allowTimesFinal})
  }
  // Optionally add "allowDates: ["25.10.2022"], formatDate: 'd.m.Y'" , to allow only certain dates. For this to work, disabledDates and disabledWeekDays needs to be off/empty. 
});
