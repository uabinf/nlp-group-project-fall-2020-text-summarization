var data = []
var token = ""
console.log("injs");
jQuery(document).ready(function () {
    $('#btn-download').hide();
    $('#label_max_words').hide();
    $('#label_num_beams').hide();
    $('#max_words').hide();
    $('#num_beams').hide();
    $('#upload_section').hide();
    var slider = $('#max_words')
    var text_val = ''
    var model =''
    var input_text =''
    slider.on('change mousemove', function (evt) {
        $('#label_max_words').text('No. of words in summary: ' + slider.val())
        // alert("hello")
    })
    console.log("here");
    var slider2 = $('#num_beams')
    slider2.on('change mousemove', function (evt) {
        $('#label_num_beams').text('Beam search: ' + slider2.val())
    })

    $('input[name="input_type"]').click(function (){
        text_val = $("input[name='input_type']:checked").val();
        if(text_val=='fileUp'){
            $('#txt_input').hide();
            $('#upload_section').show();
        }
        else{
            $('#txt_input').show();
            $('#upload_section').hide();
        }
    })

    $('#input_model').change(function (){
        model = $('#input_model').val()
        if(model=="t5"){
            $('#label_max_words').show();
            $('#label_num_beams').show();
            $('#max_words').show();
            $('#num_beams').show();
        }
        else{
            $('#label_max_words').hide();
            $('#label_num_beams').hide();
            $('#max_words').hide();
            $('#num_beams').hide();
        }
    })

    $('#btn-process').on('click', function () {
        $('#input_summary').val('...making just the right summary for you')
        // alert("hey")
        if(text_val=="fileUp"){
            console.log("uploading file")
            var form_data = new FormData($('#upload_file_form')[0]);
            $.ajax({
                type: 'POST',
                url: '/uploadFile',
                data: form_data,
                contentType: false,
                cache: false,
                processData: false,
                dataType: 'json'
            }).done(function (read_file){
                console.log("in done")
                input_text = read_file['fileData'];
                num_words = $('#max_words').val()
                num_beams = $('#num_beams').val()
                console.log(input_text)
                $.ajax({
                    url: '/predict',
                    type: "POST",
                    contentType: "application/json",
                    dataType: "json",
                    
                    data: JSON.stringify({
                        "input_text": input_text,
                        "model": model,
                        "num_words": num_words,
                        "num_beams": num_beams
                    }),
                    beforeSend: function () {
                        $('.overlay').show()
                    },
                    complete: function () {
                        $('.overlay').hide()
                    }
                }).done(function (jsondata, textStatus, jqXHR) {
                    console.log(jsondata)
                    $('#input_summary').val(jsondata['response']['summary'])
                    $('#btn-download').show();
                }).fail(function (jsondata, textStatus, jqXHR) {
                    alert(jsondata['responseJSON']['message'])
                });
                // console.log(input_text)
            }).fail(function (read_file){
                console.log("fail")
                alert(read_file)
            });
            console.log("file ready")
        }
        else{
            input_text = $('#txt_input').val()
            num_words = $('#max_words').val()
            num_beams = $('#num_beams').val()
            console.log(input_text)
            $.ajax({
                url: '/predict',
                type: "POST",
                contentType: "application/json",
                dataType: "json",
                
                data: JSON.stringify({
                    "input_text": input_text,
                    "model": model,
                    "num_words": num_words,
                    "num_beams": num_beams
                }),
                beforeSend: function () {
                    $('.overlay').show()
                },
                complete: function () {
                    $('.overlay').hide()
                }
            }).done(function (jsondata, textStatus, jqXHR) {
                console.log(jsondata)
                $('#input_summary').val(jsondata['response']['summary'])
                $('#btn-download').show();
            }).fail(function (jsondata, textStatus, jqXHR) {
                alert(jsondata['responseJSON']['message'])
            });
        }
        // model = $('#input_model').val()
        
    })



})