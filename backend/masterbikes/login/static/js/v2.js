
var cant = 0;
$(document).ready(function(){
    $('#enviarID').attr('disabled', true);

    // alert("automatico!!!");
    // cant = $("#bicicletasID").length;
    // alert(cant);
    
});

$("#agregarID").click(function(){
    // cant = $("#bicicletasID").length;
    var cant = document.getElementById("carritoID").length;

    // alert(cant);

    if (cant > 0){
        $('#enviarID').attr('disabled', false);
        
        $("#temporalID").remove();
        $("#mensajeID").append("<div id='temporalID' class='correcto'>" + "¡Correcto!"
        + "</div>");
    }else{

    }


});

$("#eliminarID").click(function(){
    // cant = $("#bicicletasID").length;
    var cant = document.getElementById("carritoID").length;

    // alert(cant);

    if (cant > 0){
        $('#enviarID').attr('disabled', false);
    }else{
        $('#enviarID').attr('disabled', true);

        $("#temporalID").remove();
        $("#mensajeID").append("<div id='temporalID'>" + "Error. Debe arrendar al menos una bicicleta."
        + "</div>");
    }
});


/**
 * 
 * 
 * 
 * 

$("#fechaInicioID").change(function(){
    alert(Date.now());
});



$("#agregarID").click(function(){
    alert("sigue funcionando");
});


 */