$(document).ready(function () {

    $.ajax({
        url: "http://localhost:9000/detalle_propiedad/" + id_propiedad,
        type: "GET",
        dataType: "json",
        success: function (response) {
            console.log('llegó!')
        }
    });
});