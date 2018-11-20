$("#Subform").on("click",function(){
alert("----------------------")
$.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
$.ajax({
    async:false,
    type:'POST',
    url: '/singe_submit',
    dataType:'json',
    //data:$('#submitpaper').serialize(),
    data: {
        'stda':$('#stda').val(),
        'tags_1':$('#tags_1').val(),
        },
    success:function(data){
    //console.log(result);
        alert(data);
    if(result.resultCode == 'ok') {
        alert("SUCCESS");
    }
    },
    error:function(){
    alert("error");
    }
});
})



