jQuery('#datepicker').datetimepicker({
    format:'d.m.Y H:i',
    inline:true,
    lang:'en',
    step: 5,
    todayButton: true,
    allowTimes: [
      '10',
      '11',
      '12',
      '13',
      '15',
      '16',
    ],
    disabledWeekDays: [
      0, 2, 3, 4, 6
    ],
  //   disabledDates: {
  //   disabledDates: [
  //     '27.10.2022'
  //   ], formateDate: 'd.m.Y'
  // },
    
  });