// Hazme una función para ver si al ingresar a login.html existe un access_token o refresh_token
// en el localStorage. Si existe, borrar el access_token y el refresh_token del localStorage.

if (localStorage.getItem('access_token') != null) {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
}

var url_api = "http://localhost:9000/"
var ep_login = "login/";
$('#btnIngresar').click(function (){
    let datos = datosIngreso()
    $.ajax({
        type : "POST",
        url : url_api + ep_login,
        data : datos,
        contentType: "application/json; charset=utf-8",
        dataType : "json",
        success : function (response) {
            localStorage.setItem('access_token', response.access);
            localStorage.setItem('refresh_token', response.refresh);
            var access = localStorage.getItem('access_token');
            decodedToken = jwt_decode(access)
            if (decodedToken['id_perfil'] === 1) {
                window.location.href = "/app/administrador"
            } else if (decodedToken['id_perfil'] === 2){
                window.location.href = "/app/usuario"
            }
        },
        error : function (errorThrown) {
            var errorMessage = "Error: " + errorThrown;
            console.log(errorMessage);
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