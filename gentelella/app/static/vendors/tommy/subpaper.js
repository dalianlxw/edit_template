$("#subpaper").on("click",function(){
 
    var fileObj = document.getElementById("file").files[0];
/*    var formfile = new FormData();
    formfile.append("file",fileObj)

   form.append("edition":$('#edition').val());
   form.append("subject",$('#subject').val());
    form.append("grade",$('grade').val());
    form.append("paper_type",$('paper_type').val());
    form.append("chapter",$('chapter').val());
    form.append("file",$("#file").get(0).files[0]); */
    alert(fileObj)
$.ajax({
    async:false,
    type:'POST',
    url: '/form_upload',
    dataType:'json',
    success:function(data){
    //console.log(result);
        alert(data);
    },
    error:function(){
    alert(data);
    alert("error");
    },
});
//$("#sub_reset")[0].reset();
//$("#Subform")[0].reset();
//$("#submitpaper")[0].reset();
    //$("input[type=reset]").trigger("click");
})