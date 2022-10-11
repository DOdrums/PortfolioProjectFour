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