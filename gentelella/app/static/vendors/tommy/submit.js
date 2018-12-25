
var cities = [
["大连","丹东","沈阳"],
["浦东","崇明","静安"]
];

$("#Subform").on("click",function(){
$.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
$.ajax({
    async:false,
    type:'POST',
    url: '/singe_submit',
    data: {
    "editor-two":$('#editor-two').val(),
    "stda":$('#stda').val(),
    "tags_1_tagsinput":$('#tags_1_tagsinput').val(),
    },
    dataType:'json',
    success:function(data){
    if (data.status == 1){
        alert("试题已经录入，确定后继续");
        $("#demo-form2")[0].reset();
    }
    else if (data.status == 0){
        alert("传数据时出现异常")
       // window.location.href="/read_file/"+data.id;
    }else{
        alert(data.status);
    }},
    error: function(XMLHttpRequest, textStatus, errorThrown) {
        alert(XMLHttpRequest.status);
        alert(XMLHttpRequest.readyState);
        alert(textStatus);
    },
});
//$("#sub_reset")[0].reset();
//$("#Subform")[0].reset();
$("#submitpaper")[0].reset();
    //$("input[type=reset]").trigger("click");
})

$(document).ready(function(){
$("#sheng").change(function(){
    $('#city').get(0).length = 0;
    var sheng = $(this).val();
    //alert(sheng);
    $.each(cities,function(i,n){
      //  alert(n)
        if(sheng == i){
            $(n).each(function(j,m){
        //    alert(m);
            $('#city').append("<option name='city'>"+ m +"</option>")
            });
        }
     });
   })
$("#subject1").change(function(){
    var edition = $("#edition").val();
    var subject = $(this).val();
    alert(edition);

    })
$("#grade").change(function(){
    var edition =$("#edition").val();
    var subject =$("#subject").val();
    var grade = $(this).val();
   // var paper_type = $("#paper_type").val();
   // alert(edition + grade + subject + '-----');
    $.post("get_chapter",
    {
        edition:edition,
        subject:subject,
        grade:grade,
//        paper_type:paper_type
    },
    function(data,status){
        $('#chapter').empty();
//        console.log(toString.call(data));
        $.each(data,function(i,item){
           //   console.log(item.id,item.chapterorder,item.chapter);
              $('#chapter').append("<option value=" + item.id + ">第"+ item.chapterorder +"章----"  + item.chapter + "</option>")
        })
     })
    })
 })

