var url_api = "http://localhost:9000/"
var ep_token = "api/registro/";
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
        email : $('#regCorreo').val(),
        password : $('#registroPassword').val(),
        first_name : $('#regNombre').val(),
        last_name : $('#regApellido').val()
    }
    return JSON.stringify(dicc)
}

function checkPassword() {

}