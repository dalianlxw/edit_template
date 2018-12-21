$('#subpaper').on('click', function() {
    var file_data = $('#upfile').prop('files')[0];
    var file_info = $('#upfile')[0].files[0];   
    var form_data = new FormData();                  
    form_data.append('file', file_data);
    form_data.append('file1',file_info);
    alert(form_data);                             
    $.ajax({
        url: 'form_test', // point to server-side PHP script 
        dataType: 'json',  // what to expect back from the PHP script, if anything
        cache: false,
        contentType: false,
        processData: false,
        data: form_data,                         
        type: 'post',
        success: function(data){
            if (data.status = 200)
                alert(data.mesg); // display response from the PHP script, if any
            else
                alert(data.status)
        },
        error:function(){
            alert('error')
        },
     });
});