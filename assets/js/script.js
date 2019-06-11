jQuery.datetimepicker.setLocale('nl');
$(function () {
    $("#id_date").datetimepicker({
        i18n:{
     de:{
      months:[
       'Januari','Februari','Maart','April',
       'Mei','Juni','Juli','Augustus',
       'September','Oktober','November','December',
      ],
      dayOfWeek:[
       "Zo.", "Mo", "Di", "Moe",
       "Do", "Fr", "Za.",
      ]
     }
    },
      format: 'd/m/Y H:i',
      // inline:true,
      // datetimepicker:false,
      allowTimes:[
          '09:30', '10:00', '11.15',
          '12:00', '13:00', '15:15',
          '16:00',
         ]
    });
  });
