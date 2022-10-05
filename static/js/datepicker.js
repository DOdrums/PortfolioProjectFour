jQuery('#datepicker').datetimepicker({
    format:'d.m.Y H:i',
    inline:true,
    lang:'en',
    step: 5,
    todayButton:true,
    allowTimes: [
      '10:00',
      '10:15',
      '10:30',
      '11:15',
      '12:00',
      '13:00',
      '15:30',
      '15:45',
      '16:00',
    ],
    disabledWeekDays: [
      0, 2, 3, 4, 6
    ],
    disabledDates: [
      '28.10.2022'
    ], formatDate: 'd.m.Y'
  });