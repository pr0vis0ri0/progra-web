function cerrarSesion () {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    window.location.href = "/app/login";
}