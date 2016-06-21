/**
 * Created by emanuelziga on 17/6/16.
 */
(function($) {
    $(document).ready(function($) {

// SELECTORS

    var sell_price = $('#id_product_sellprice');

    var use_inv = $('#id_product_useinventory');
    var div_inventory = $('.field-product_inventory');
    var div_min_inventory = $('.field-product_minimum');

    var autoprice = $('#id_product_autoprice');
    var div_utility = $('.field-product_utility');
    var div_price = $('.field-product_price');

    var use_taxes = $('#id_product_usetaxes');
    var div_taxes = $('.field-product_taxes');


//SELECTORS END

    //sell_price.prop('disabled', true);

// FIELDS HIDE AND SHOW

//USE INVENTORY FIELDS
    if(use_inv.is(':checked')==false){

        div_inventory.hide();
        div_min_inventory.hide();
    }

    use_inv.change(function() {//USE INVENTORY TOGGLE

        if(use_inv.is(':checked')){
            div_inventory.show();
            div_min_inventory.show();
        }
        else {
            div_inventory.hide();
            div_min_inventory.hide();
        }
    });//USE INVENTORY ENDS

//AUTO PRICE FIELDS
    if(autoprice.is(':checked')==false){

        div_utility.hide();
        div_price.show();
    }
    else{
        div_utility.show();
        div_price.hide();
    }

    autoprice.change(function() {//AUTO PRICE TOGGLE

        if(autoprice.is(':checked')){
            div_utility.show();
            div_price.hide();
        }
        else {
            div_utility.hide();
            div_price.show();
        }

        SetSellPrice();
    });// AUTO PRICE TOGGLE ENDS

//USE TAXES FIELDS
    if(use_taxes.is(':checked')==false){

        div_taxes.hide();

    }
    use_taxes.change(function() {//USE TAXES TOGGLE

        if(use_taxes.is(':checked')){
            div_taxes.show();
        }
        else {
            div_taxes.hide();
        }
    });// USE TAXES TOGGLE ENDS


    });//document ready closes

    function SetSellPrice (){

        var sell_price = $('#id_product_sellprice');
        var cost = $('#id_product_cost');
        var autoprice = $('#id_product_autoprice');
        var utility = $('#id_product_utility');
        var price = $('#id_product_price');
        var use_taxes = $('#id_product_usetaxes');
        var taxes = $('#id_product_taxes');

        var price_to_set = 0;

        if(autoprice.is(':checked')){
            price_to_set = cost.val()*(1+(utility.val()/100));
        }
        else{
            console.log(price.val());
            price_to_set = price.val();
        }

        sell_price.val(parseFloat(price_to_set).toFixed(2));
    }
})(django.jQuery);