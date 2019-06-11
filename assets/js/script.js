$(function () {
    $("#id_date").datetimepicker({

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
 // $("#id_date").on('click',function(e){
 //     var data = $(this).val();
 //    console.log("data",data);
 // })
