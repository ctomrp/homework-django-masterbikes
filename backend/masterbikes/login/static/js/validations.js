$(document).on("input", () => {
        
    const nombreIn = $("#id_username").val().trim();
    const nombreSpan =  $("#nameSpan");
    const passwordIn = $("#id_password1").val().trim();
    const passwordSpan = $("#passwordSpan");
    const passwordIn2 = $("#id_password2").val().trim();
    const passwordSpan2 = $("#passwordSpan2");
    const emailIn = $("#id_email").val().trim();
    const emailSpan = $("#emailSpan")

    const btn = $("#register");
    
    function validarNombre(nombre){
        return nombre.length >= 3 && nombre.length <= 15;
    }
    
    function validarPass(pass){
        return pass.length >= 3 && pass.length <= 15;
    }
    
    function validarEmail(email){
        const re = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
        return re.test(email);
    }

    if(validarNombre(nombreIn)){
        nombreSpan.text('');
        $("#id_username").addClass("is-valid");
        $("#id_username").removeClass("is-invalid");
    }else{
        nombreSpan.text('Debe tener entre 3 y 15 caracteres');
        $("#id_username").removeClass("is-valid");
        $("#id_username").addClass("is-invalid");
    }

    if(validarPass(passwordIn)){
        passwordSpan.text('');
        $("#id_password1").addClass("is-valid");
        $("#id_password1").removeClass("is-invalid");
    }else{
        passwordSpan.text('Debe tener entre 3 y 15 caracteres');
        $("#id_password1").removeClass("is-valid");
        $("#id_password1").addClass("is-invalid");
    }

    if(validarPass(passwordIn2)){
        passwordSpan2.text('');
        $("#id_password2").addClass("is-valid");
        $("#id_password2").removeClass("is-invalid");
    }else{
        passwordSpan2.text('Debe tener entre 3 y 15 caracteres');
        $("#id_password2").removeClass("is-valid");
        $("#id_password2").addClass("is-invalid");
    }

    if(validarEmail(emailIn)){
        emailSpan.text('Correo válido');
        $("#emailSpan").css('color', "green");        
    }else{
        emailSpan.text('Correo inválido');
        $("#emailSpan").css('color', "red");        

    }

    function validarFormulario(){
        if(validarNombre(nombreIn) && validarPass(passwordIn) && validarPass(passwordIn2) && validarEmail(emailIn)){
            btn.prop("disabled",false);
        }else{
            btn.prop("disabled",true);
        }
    }

    validarFormulario();

});
