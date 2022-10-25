var disabledWeekDays = planningJS.disabled_weekdays.split(",")
var disabledWeekDaysList = disabledWeekDays.map(function (x) {
  return parseInt(x, 10)
})

document.getElementById('id_treatment_name').addEventListener('change', setTreatment, true);
function setTreatment(e) {
  console.log(e.target.value)
}

dateToday = new Date()
var allowTimesFinal = planningJS.allow_times.split(",")
getBlockedTimesList(dateToday)

function getAllowdTimesList(date) {
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
  let allowedTimesList = getAllowdTimesList(selectedDate.toISOString())

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