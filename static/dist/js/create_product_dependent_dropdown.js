$(document).ready(function(){

 var category = $("#category_ddl");
 var Product = $("#Product_ddl");
 var $options = Product.find('option');
 category.on('change',function(){
    create.html($options.filter('[value="'+ this.value  +'"]'));
 }).trigger('change');

});

