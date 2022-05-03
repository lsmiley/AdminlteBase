$(document).ready(function(){

 var category = $("#category");
 var Product = $("#Product");
 var $options = Product.find('option');
 category.on('change',function(){
    create.html($options.filter('[value="'+ this.value  +'"]'));
 }).trigger('change');

});