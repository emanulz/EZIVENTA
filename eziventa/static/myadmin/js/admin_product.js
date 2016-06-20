/**
 * Created by emanuelziga on 17/6/16.
 */
(function($) {
    $(document).ready(function($) {

    var use_inv = $('#id_product_useinventory');
    var div_inventory = $('.field-product_inventory');
    var div_min_inventory = $('.field-product_minimum');

    if(use_inv.is(':checked')==false){

        div_inventory.hide();
        div_min_inventory.hide();

    }

    use_inv.change(function() {


        if(use_inv.is(':checked')){
            div_inventory.show();
            div_min_inventory.show();
        }
        else {
            div_inventory.hide();
            div_min_inventory.hide();

        }


    });


    });
})(django.jQuery);