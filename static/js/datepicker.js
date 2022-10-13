var disabledWeekDays = planningJS.disabled_weekdays.split(",")
var disabledWeekDaysList = disabledWeekDays.map(function (x) {
  return parseInt(x, 10)
})

var allowTimes = [];

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

function getBlockedTimesList() {
  let allowedTimesList = getAllowdTimesList("2022-10-17T09:54:05+00:00")

  appointments.forEach(element => {
    element.date_time = new Date(element.date_time);
    let startTime = element.date_time
    let endTime = new Date(element.date_time.getTime() + element.duration*60000)
    for (time of allowedTimesList) {
      if (startTime <= time && time < endTime) {
        allowedTimesList = allowedTimesList.filter(e => e !== time);
      }
    }
  });
  let blockedTimesList = allowedTimesList
  convertBlockedTimesList(blockedTimesList)
}

function convertBlockedTimesList(blockedTimesList) {
  for (dateTime of blockedTimesList) {
    let time = dateTime.getHours() + ":" + dateTime.getMinutes();
    allowTimes.push(time)
  }
}

getBlockedTimesList()

jQuery('#datepicker').datetimepicker({
  format:'d.m.Y H:i',
  inline:true,
  lang:'en',
  step: 5,
  todayButton:true,
  allowTimes: allowTimes, 
  disabledWeekDays: disabledWeekDaysList,
  disabledDates: planningJS.disabled_dates.split(","), formatDate: 'd.m.Y',
  // Optionally add "allowDates: ["25.10.2022"], formatDate: 'd.m.Y'" , to allow only certain dates. For this to work, disabledDates and disabledWeekDays needs to be off/empty. 
});
