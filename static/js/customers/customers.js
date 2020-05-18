$(document).ready(function(){
    function update_states(form_id, country_id){
        $.ajax({
            type: "GET",
            url: '/customers/fetch-data',
            data: {'country_id': country_id},
            success: function(result) {
                $('select[name="form-'+form_id+'-state"]').empty()
                data = JSON.parse(result)
                $.each(data, function(key, value) {   
                    $('select[name="form-'+form_id+'-state"]')
                        .append($("<option></option>")
                                .attr("value",value.pk)
                                .text(value.fields.name)
                        ); 
               });
            }, 
            
        });
    }

    function update_cities(form_id, state_id){
        $.ajax({
            type: "GET",
            url: '/customers/fetch-data',
            data: {'state_id': state_id},
            success: function(result) {
                $('select[name="form-'+form_id+'-city"]').empty()
                data = JSON.parse(result)
                $.each(data, function(key, value) {   
                    $('select[name="form-'+form_id+'-city"]')
                        .append($("<option></option>")
                                .attr("value",value.pk)
                                .text(value.fields.name)
                        ); 
               });
            }, 
            
        });
    }

    $(".select-country").change(function(){
        var form_id = $(this).parent().parent().parent().children()[1].value
        update_states(form_id, $(this).val())
    });

    $(".select-state").change(function(){
        var form_id = $(this).parent().parent().parent().children()[1].value
        update_cities(form_id, $(this).val())
    });

    // $(".customer_form").validate({
    // })
    
    $('#billing_address').on('click', function() {
        if ($('select[name="form-0-state"]').val() != "" && $('select[name="form-0-city"]').val() != ""){
            update_states('1', $('select[name="form-0-country"]').val())
            update_cities('1', $('select[name="form-0-state"]').val())
        }
       
        $('select[name="form-1-country"]').val($('select[name="form-0-country"]').val())
        $('select[name="form-1-state"]').val($('select[name="form-0-state"]').val())
        $('select[name="form-1-city"]').val($('select[name="form-0-city"]').val())
        $('textarea[name="form-1-street_address1"]').val($('textarea[name="form-0-street_address1"]').val())
        $('textarea[name="form-1-street_address2"]').val($('textarea[name="form-0-street_address2"]').val())
        $('input[name="form-1-name"]').val($('input[name="form-0-name"]').val())
        $('input[name="form-1-post_office_box"]').val($('input[name="form-0-post_office_box"]').val())
        $('input[name="form-1-zip_code"]').val($('input[name="form-0-zip_code"]').val())
    });
    
})