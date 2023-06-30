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
            console.log(response)
            localStorage.setItem('token', response['access'])
            window.location.href = 'http://localhost:8000/app/redirigir'
        },
        error : function () {
            console.log('El login ha fallado')
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