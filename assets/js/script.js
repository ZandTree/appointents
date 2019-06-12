(function(){
        var csrf_token = Cookies.get('csrftoken');
        console.log('where is my token:',csrf_token);
        $.ajaxSetup(
            {headers:{'X-CSRFToken':csrf_token}}
        );
    })();

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
      startDate:'+2019/06/12',//or 1986/12/08,
      allowTimes:[
          '09:30', '10:00', '11.15',
          '12:00', '13:00', '15:15',
          '16:00',
         ]
    });
  });
  $("#app").on('submit',function(e){
      e.preventDefault();
      // console.log("form submited");
      var url = $(this).attr("action");
      // var data = $("#id_date").val();
      $.ajax({
          url:url,
          data:$(this).serialize(),
          type:$(this).attr('method'),
          success:function(resp){
              console.log('resp sent');
          },
          error:function(err){
              console.log("err",err);
          }


      })
  })
