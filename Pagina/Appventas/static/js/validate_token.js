if ("token" in localStorage === false ){
    window.location.href = "/app/inicio"
} else {
    var url_api = "http://localhost:9000/"
    var ep_token = "api/token/verify/";
    let datos = datosToken()
    $.ajax({
        type : "POST",
        url : url_api + ep_token,
        data : datos,
        contentType: "application/json; charset=utf-8",
        dataType : "json",
        success : function (response) {
            console.log(response)
        },
        error : function () {
            window.location.href = "/app/inicio"
        }
    })
}