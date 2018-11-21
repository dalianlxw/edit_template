$("#Subform").on("click",function(){
$.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
$.ajax({
    async:false,
    type:'POST',
    url: '/singe_submit',
    data: {
    "editor-one":$('#editor-one').val(),
    "stda":$('#stda').val(),
    "tags_1":$('#tags_1').val(),
    "subject_ver":$('#subject_ver').val()
    },
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
$("#submitpaper")[0].reset();
    //$("input[type=reset]").trigger("click");
})



