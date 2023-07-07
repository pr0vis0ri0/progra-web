var url_api = "http://localhost:9000/"
var ep_token = "registro/";
$('#btnRegistrar').click(function (){
    let datos = datosRegistro()
    $.ajax({
        type : "POST",
        url : url_api + ep_token,
        data : datos,
        contentType: "application/json; charset=utf-8",
        dataType : "json",
        success : function (response) {
            console.log(response)
            console.log('Registro creado')
        },
        error : function () {
            $('#regCorreo').addClass('is-invalid')
            $('#registroPassword').addClass('is-invalid')
            $('#checkPassword').addClass('is-invalid')
            $('#regNombre').addClass('is-invalid')
            $('#regApellido').addClass('is-invalid')
        }
    })
});

function datosRegistro () {
    dicc = {
        username : $('#regCorreo').val(),
        password : $('#registroPassword').val(),
        email : $('#regCorreo').val(),
        first_name : $('#regNombre').val(),
        last_name : $('#regApellido').val()
    }
    return JSON.stringify(dicc)
}

$(document).on("click blur change focusout select", 
                "#regNombre, #regApellido, #regCorreo, #registroPassword, #checkPassword",
    function () {
      checkFormularioRegistro();
    }
);

function checkFormularioRegistro () {
    var error = 0

    if ($('#regNombre').val() == "") {
        $('#regNombre').addClass('is-invalid')
        error = 1
    } else {
        $('#regNombre').removeClass('is-invalid')
        $('#regNombre').addClass('is-valid')        
    }

    if ($('#regApellido').val() == ""){
        $('#regApellido').addClass('is-invalid')
        error = 1
    } else {
        $('#regApellido').removeClass('is-invalid')
        $('#regApellido').addClass('is-valid')
    }

    if($('#regCorreo').val() == "") {
        $('#regCorreo').addClass('is-invalid')
        error = 1
    } else {
        $('#regCorreo').removeClass('is-invalid')
        $('#regCorreo').addClass('is-valid')
    }
    
    if($('#registroPassword').val() == "") {
        $('#registroPassword').addClass('is-invalid')
        error = 1
    } else if ($('#registroPassword').val().length < 8) {
        $('#registroPassword').addClass('is-invalid')
        error = 1 
    } else {
        $('#registroPassword').removeClass('is-invalid')
        $('#registroPassword').addClass('is-valid')
    }

    if($('#checkPassword').val() == "") {
        $('#checkPassword').addClass('is-invalid')
        error = 1
    } else {
        $('#checkPassword').removeClass('is-invalid')
        $('#checkPassword').addClass('is-valid')
    }

    if ($('#checkPassword').val() != $('#registroPassword').val() || $('#checkPassword').val() == "") {
        $('#checkPassword').addClass('is-invalid')
        error = 1
    } else {
        $('#checkPassword').removeClass('is-invalid')
        $('#checkPassword').addClass('is-valid')
    }

    if (error == 1) {
        $('#btnRegistrar').addClass('disabled')
                            .prop("disabled", true)
                            .each(function() {
                                this.style.pointerEvents = "none"
                            })
    } else {
        $('#btnRegistrar').removeClass('disabled')
                            .prop("disabled", false)
                            .each(function() {
                                this.style.pointerEvents = "auto"
                            })
    }
}