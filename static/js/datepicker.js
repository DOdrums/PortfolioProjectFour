jQuery('#datepicker').datetimepicker({
    format:'d.m.Y H:i',
    inline:true,
    lang:'en',
    step: 5,
    todayButton:true,
    allowTimes: planningJS.allow_times.split(","), 
    disabledWeekDays: [
        0, 2, 3, 4, 6
      ],
    disabledDates: planningJS.disabled_days.split(","), formatDate: 'd.m.Y',
    allowDates: ["25.10.2022"], formatDate: 'd.m.Y'
    // Optionally add "allowDates: ["25.10.2022"], formatDate: 'd.m.Y'" , to allow only certain dates. For this to work, disabledDates and disabledWeekDays needs to be off. 
  });