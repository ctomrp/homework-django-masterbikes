
$("#tipo1").click(function(){

    alert('hola');

});


var grupo = "2";
var bicis = "";
$("#agregarID").click(function(){

    var sel = $("#bicicletasID :selected");
    var val = $(sel).val();
    var text = $(sel).text();
    var idPadre = sel.parent().prop("id");
    grupo = "#" + idPadre.substr(0, idPadre.length - 1) + "2";
    //alert(grupo);

    $(grupo).append('<option value="' + val + '">' + text + '</option>');

    bicis = bicis + val + ",";
    $("#ocultoID").text(bicis);
    //var val = "#bicicletasID option[value=" + val + "]";

    $(sel).remove();

});


$("#eliminarID").click(function(){

    var sel = $("#carritoID :selected");
    var val = $(sel).val();
    var text = $(sel).text();
    var idPadre = sel.parent().prop("id");
    grupo = "#" + idPadre.substr(0, idPadre.length - 1) + "1";
    // alert(grupo);

    $(grupo).append('<option value="' + val + '">' + text + '</option>');

    bicis = bicis.replace(val + ',', '');
    //var val = "#bicicletasID option[value=" + val + "]";
    $("#ocultoID").text(bicis);


    $(sel).remove();

});



/**
 * 
 * 
 * 


$(document).ready(function(){

    $("#tabla1id").append("1" +
        "2");

});


$("#eliminarID").click(function(){

    var val = $("#carritoID :selected").val();
    var text = $("#carritoID :selected").text();
    $("#bicicletasID").append('<option value="' + val + '">(' + val + ')' + text + '</option>');

    var val = "#carritoID option[value=" + val + "]";
    $(val).remove();

    
});


 * 
 */
