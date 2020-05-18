$(document).ready(function(){

    /* Tax Form Actions Starts */
    $("#create_tax").validate();

    $('.tax_edit').on('click', function() {
        let url = $(this).data('url');
        let form_action = $(this).data('update');
        $.ajax({
            type: "GET",
            url: url,
            success: function(result) {
                if(result.length != 0){
                    data = result[0];
                    $('#create_tax input[name="company"]').val(data.company__pk);
                    $('#create_tax input[name="name"]').val(data.name);
                    $('#create_tax input[name="percentage"]').val(data.percentage);
                    $('#create_tax textarea[name="description"]').val(data.description);
                    $("#add_tax").text("Update Tax");
                    $(".add_new_tax").click();
                    $('#create_tax').attr('action', form_action);
                }
            },
        });
    });

    /* reset tax modal form */
    $('#tax_modal_form').on('hidden.bs.modal', function (e) {
        $('#create_tax').trigger("reset");
        $('#create_tax').attr('action', '/settings/tax/create');
        $("#add_tax").text("Add Tax");
    });
    /* Tax Form Actions Ends */


    /* Category Form Actions Starts */
    $("#create_category").validate();

    $('.catgry_edit').on('click', function() {
        let url = $(this).data('url');
        let form_action = $(this).data('update');
        $.ajax({
            type: "GET",
            url: url,
            success: function(result) {
                if(result.length != 0){
                    data = result[0];
                    $('#create_category input[name="company"]').val(data.company__pk);
                    $('#create_category input[name="name"]').val(data.name);
                    $('#create_category textarea[name="description"]').val(data.description);
                    $("#add_category").text("Update Category");
                    $(".add_new_category").click();
                    $('#create_category').attr('action', form_action);
                }
            },
        });
    });
    
    /* reset category modal form */
    $('#category_modal_form').on('hidden.bs.modal', function (e) {
        $('#create_category').trigger("reset");
        $('#create_category').attr('action', '/settings/category/create');
        $("#add_category").text("Add Category");
    });
    /* Category Form Actions Ends */

    /* Documents Form Actions Starts */
    $("#upload_document").validate();

    $('.document_edit').on('click', function() {
        let url = $(this).data('url');
        let form_action = $(this).data('update');
        $.ajax({
            type: "GET",
            url: url,
            success: function(result) {
                if(result.length != 0){
                    data = result[0];
                    $('#upload_document input[type="file"]').val(data.document);
                    $('#upload_document textarea[name="description"]').val(data.description);
                    $("#add_doc").text("Update Document");
                    $(".add_new_doc").click();
                    $('#upload_document').attr('action', form_action);
                }
            },
        });
    });
    /* Documents Form Actions Ends */

    /* Unit Form Actions Starts */
    $("#create_unit").validate();

    $('.unit_edit').on('click', function() {
        let url = $(this).data('url');
        let form_action = $(this).data('update');
        $.ajax({
            type: "GET",
            url: url,
            success: function(result) {
                if(result.length != 0){
                    data = result[0];
                    $('#create_unit input[name="company"]').val(data.company__pk);
                    $('#create_unit input[name="name"]').val(data.name);
                    $('#create_unit textarea[name="description"]').val(data.description);
                    $("#add_unit").text("Update Unit");
                    $(".add_new_unit").click();
                    $('#create_unit').attr('action', form_action);
                }
            },
        });
    });
    
    /* reset unit modal form */
    $('#unit_modal_form').on('hidden.bs.modal', function (e) {
        $('#create_unit').trigger("reset");
        $('#create_unit').attr('action', '/settings/unit/create');
        $("#add_unit").text("Add Unit");
    });
    /* Unit Form Actions Ends */
});
