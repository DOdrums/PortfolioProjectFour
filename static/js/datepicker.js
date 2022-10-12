var disabledWeekDays = planningJS.disabled_weekdays.split(",")
var disabledWeekDaysList = disabledWeekDays.map(function (x) {
  return parseInt(x, 10)
})

jQuery('#datepicker').datetimepicker({
    format:'d.m.Y H:i',
    inline:true,
    lang:'en',
    step: 5,
    todayButton:true,
    allowTimes: planningJS.allow_times.split(","), 
    disabledWeekDays: disabledWeekDaysList,
    disabledDates: planningJS.disabled_dates.split(","), formatDate: 'd.m.Y',
    // Optionally add "allowDates: ["25.10.2022"], formatDate: 'd.m.Y'" , to allow only certain dates. For this to work, disabledDates and disabledWeekDays needs to be off/empty. 
  });


appointments.forEach(element => {
  let timeoption = element.date_time.split("T").shift()
  time = "09:15"
  timeoption = timeoption + "T" + time
  timeoption = new Date (timeoption)
  console.log(timeoption)
  element.date_time = new Date(element.date_time);
  let startTime = element.date_time
  let endTime = new Date(element.date_time.getTime() + element.duration*60000)
  console.log(startTime)
  console.log(endTime)
  if (startTime < timeoption && timeoption < endTime) {
    console.log("not valid")
  }
});

console.log(appointments)

// Turn all times in allowTimes into data objects. Than make start and endtimes for each appointment, than check if any allowTimes fall in between start and endtimes and remove if they do. Return a new list with removed times. 
  