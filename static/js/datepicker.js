jQuery('#datepicker').datetimepicker({
    format:'d.m.Y H:i',
    inline:true,
    lang:'en',
    step: 5,
    todayButton:true,
    allowTimes: times, 
    disabledWeekDays: [
      0, 2, 3, 4, 6
    ],
    disabledDates: d_dates, formatDate: 'd.m.Y'
  });