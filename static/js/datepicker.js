if (document.documentElement.clientWidth < 768) {
  document.getElementById('datepicker-enable-right').id = 'datepicker'
} else {
  document.getElementById('datepicker-enable-left').id = 'datepicker'
}

var timePicked = false
var datePicked = false
var disabledWeekDays = planningJS.disabled_weekdays.split(",")
var disabledWeekDaysList = disabledWeekDays.map(function (x) {
  return parseInt(x, 10)
})

document.getElementById('id_date_time').disabled = true;
document.getElementById('booking_form').addEventListener("submit", submitForm) 
function submitForm() {
  document.getElementById('id_date_time').disabled = false;
}

var selectedDate = new Date()
var allowTimesFinal = planningJS.allow_times.split(",")
// get allowedTimes entered in admin panel by site owner.

// get endTime, the time at which the workday ends.
var selectedTreatmentDuration = 180

getBlockedTimesList(selectedDate)
// get allowedTimes with currently booked appointments blocking times.
// this is done per day, so the list changes when a new date is selected.

document.getElementById('id_treatment_name').addEventListener('change', setTreatment, true);
// get value from selected treatment option and store duration value in selectedTreatmentDuration
function setTreatment(e) {
  document.getElementById('datepicker-cover-left').style.display = "none";
  document.getElementById('datepicker-cover-right').style.display = "none";
  selectedTreatmentDuration = parseInt(e.target.value.split(",")[1])
  getBlockedTimesList(selectedDate)
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
  // Compares times in allowedTimes with appointments. Block out any
  // times that appointments are scheduled. Also checks for selected treatments
  // duration, making sure the appointment can't be scheduled with an end time
  // later than the registered endtime by sitowner.
  let allowedTimesList = getAllowdTimesListWithDate(selectedDate.toISOString())
  var workDayEndTime = allowedTimesList[allowedTimesList.length - 1]

  appointments.forEach(element => {
    // loop over all appointments in the database
    appDate = new Date(element.date_time)

    if (appDate.toDateString() === selectedDate.toDateString()) {
      // select any appointments that fall on the selected date
      let appStartTime = appDate
      let appEndTime = new Date(appDate.getTime() + element.duration*60000)
      for (time of allowedTimesList) {
        // loop over all the times to see which times should be bookable
        let treatmentEndTime = new Date(time.getTime() + selectedTreatmentDuration*60000)
        if (treatmentEndTime > workDayEndTime) {
          // first we block off any times that cause the selected treatment to run later than
          // the end of the workday
          allowedTimesList = allowedTimesList.filter(e => e !== time);
        }
        if (time < appEndTime) {
          // then we select all the times before the end of a appointment
          if (treatmentEndTime > appStartTime) {
            // then we see which of those times would make the selected appointment run late
            allowedTimesList = allowedTimesList.filter(e => e !== time);
          }
        }
      }
      // if time + duration is > than starttime, remove all times before
      // check treatmentEndTime UNTIL endtime, than go to next appointment

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
      $('#datepicker').datetimepicker('setOptions', {allowTimes: allowTimesFinal})
    }
}
function setSelectedDate(date) {
  dateString = `${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()} ${date.getHours()}:${date.getMinutes()<10?'0':""}${date.getMinutes()}`
  $('#id_date_time').val(dateString)
}

function clearSelectedDate() {
  $('#id_date_time').val("")
}

jQuery('#datepicker').datetimepicker({
  format:'c',
  inline:true,
  lang:'en',
  defaultSelect:false,
  todayButton:true,
  minDate: new Date,
  allowTimes: allowTimesFinal,
  disabledWeekDays: disabledWeekDaysList,
  disabledDates: planningJS.disabled_dates.split(","), formatDate: 'd.m.Y',
  onChangeDateTime: function(dp, $input) {
    selectedDate = new Date($input.val());
    getBlockedTimesList(selectedDate);
  },
  onSelectDate: function(ct,$i) {
    selectedDate = new Date($i.val());
    datePicked = true
    if(timePicked) {
      getBlockedTimesList(selectedDate);
      time = `${selectedDate.getHours()}:${selectedDate.getMinutes()}`
      if(!(allowTimesFinal.includes(time.toString()))) {
        clearSelectedDate()
        console.log(time)
        console.log(allowTimesFinal)
      } else {
        setSelectedDate(selectedDate)
        console.log(time)
        console.log(allowTimesFinal)
      }
    }
  },
  onSelectTime: function(current_time, $input) {
    timePicked = true;
    selectedDate = new Date($input.val());
    if(datePicked) {
      setSelectedDate(selectedDate);
    }
  }
  // Optionally add "allowDates: ["25.10.2022"], formatDate: 'd.m.Y'" , to allow only certain dates. For this to work, disabledDates and disabledWeekDays needs to be off/empty. 
});


