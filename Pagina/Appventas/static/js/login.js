var url_api = "http://localhost:9000/"
var ep_token = "api/token/";
$('#btnIngresar').click(function (){
    let datos = datosIngreso()
    $.ajax({
        type : "POST",
        url : url_api + ep_token,
        data : datos,
        contentType: "application/json; charset=utf-8",
        dataType : "json",
        success : function (response) {
            $('#loginCorreo').removeClass('is-invalid')
            $('#loginPassword').removaClass('is-invalid')
            $('#loginCorreo').addClass('is-valid')
            $('#loginPassword').addClass('is-valid')
            localStorage.setItem('token', response)
            //window.location.href = 'http://localhost:8000/app/redirigir' 
        },
        error : function () {
            $('#loginCorreo').addClass('is-invalid')
            $('#loginPassword').addClass('is-invalid')
        }
    })
});

function datosIngreso () {
    dicc = {
        username : $('#loginCorreo').val(),
        password : $('#loginPassword').val()
    }
    return JSON.stringify(dicc)
}