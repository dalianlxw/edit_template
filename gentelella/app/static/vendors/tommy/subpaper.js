

$("#subpaper").on("click",function(){
    var file_data = $('#upfile').prop('files')[0];
    //var file_info = $('#upfile')[0].files[0];  文件上传另一种表达方式
    var form_data = new FormData();                  
    form_data.append('file', file_data);
    form_data.append("edition",$('#edition').val());
    form_data.append("subject",$('#subject').val());
    form_data.append("grade",$('#grade').val());
    form_data.append("paper_type",$('#paper_type').val());
    form_data.append("chapter",$('#chapter').val());
$.ajax({
    async:false,
    type:'POST',
    url: '/form_upload',
    data: form_data,
    contentType:false,
    cache:false,
    processData:false,
    dataType:'json',
    success:function(data){
    if (data.status == 1){
        alert("试卷已经录入，确定后继续");
        $("#demo-form2")[0].reset();
    }
    else if (data.status == 0){
//        alert("试卷已经保存，确定后进行编辑")
        window.location.href="/read_file/"+data.id+"/";
    }else{
        alert(data.status);
    }},
    error: function(XMLHttpRequest, textStatus, errorThrown) {
        alert(XMLHttpRequest.status);
        alert(XMLHttpRequest.readyState);
        alert(textStatus);
    }
});
//$("#sub_reset")[0].reset();
//$("#Subform")[0].reset();
//$("#demo-form2")[0].reset();
    //$("input[type=reset]").trigger("click");
})
