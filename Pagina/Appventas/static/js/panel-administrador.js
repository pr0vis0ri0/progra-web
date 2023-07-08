if (!localStorage.getItem("access_token")) {
    window.location.href = "/app/login";
} else {
    var access = localStorage.getItem('access_token');
    var decodedToken = jwt_decode(access)
    
    if (decodedToken['id_perfil'] != 1) {
        window.location.href = "/app/usuario";
    }
}