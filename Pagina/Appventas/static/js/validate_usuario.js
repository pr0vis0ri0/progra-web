token = sessionStorage.getItem('token')
decodedToken = jwt_decode(token)
if (decodedToken['es_superusuario'] === false) {
  window.location = '/index.html'
}    