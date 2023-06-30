if ("token" in localStorage === false ){
    window.location.href = "/app/inicio"
} else {
    token = localStorage.getItem('token')
    decodedToken = jwt_decode(token)
    console.log(decodedToken)
    if (decodedToken['es_superusuario'] === true) {
        window.location.href = "/app/administrador"
    } else {
        window.location.href = "/app/usuario"
    }
}