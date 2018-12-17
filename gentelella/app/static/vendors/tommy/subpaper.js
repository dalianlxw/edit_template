$("#subpaper").on("click",function(){
var data = new FormData();
data.append('file', document.getElementById("upfile"));

$.ajax({
    async:false,
    type:'POST',
    url: '/form_upload',
 //   data:$('#demo-form2').serialize(),
    data: data,
    contentType:false,
    cache:false,
    processData:false,
    dataType:'json',
    success:function(data){
    //console.log(result);
        alert(data);
    },
    error:function(){
    alert("error");
    },
});
//$("#sub_reset")[0].reset();
//$("#Subform")[0].reset();
//$("#submitpaper")[0].reset();
    //$("input[type=reset]").trigger("click");
})


 
 //   var fileObj = document.getElementById("file").files[0];
/*    var formfile = new FormData();
    formfile.append("file",fileObj)

   form.append("edition":$('#edition').val());
   form.append("subject",$('#subject').val());
    form.append("grade",$('grade').val());
    form.append("paper_type",$('paper_type').val());
    form.append("chapter",$('chapter').val());
    form.append("file",$("#file").get(0).files[0]); */
//    alert(fileObj)