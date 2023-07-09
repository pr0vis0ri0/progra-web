if (!localStorage.getItem("access_token")) {
    window.location.href = "/app/login";
} else {
    let prior_ingreso = localStorage.getItem('access_token');
    let decodedPrior = jwt_decode(prior_ingreso)
    
    if (decodedPrior['id_perfil'] == 2) {
        window.location.href = "/app/usuario";
    }
}

var url_api = "http://localhost:9000/"
var ep_prop_pendiente_admin = "adm_prop_pendientes/"
var ep_prop_base_admin = "adm_prop_base/"
var access = localStorage.getItem('access_token');
var decodedToken = jwt_decode(access)
var api = new API()

$(document).ready(function (){
    api.devolverPropPendientesAdmin(url_api + ep_prop_pendiente_admin, devolverIdUsuario())
    api.devolverPropBaseAdmin(url_api + ep_prop_base_admin, devolverIdUsuario())
})

function devolverIdUsuario () {
    data = {
        id_usuario : decodedToken['id_usuario']
    }
    return JSON.stringify(data)
}

function cargarTablas(p, tabla, agregarBotones) {
    if (Array.isArray(p)) {
        $.each(p, function(i) {
            agregarFila(p[i], tabla, agregarBotones);
        });
    } else {
        agregarFila(p);
    }
}

function agregarFila(data, tabla, agregarBotones) {
    tabla.append(
        $('<tr>')
            .append($('<td>').text(data.id_propiedad))
            .append($('<td>').text(data.nombre_usuario))
            .append($('<td>').text(data.nombre_tipo_propiedad))
            .append($('<td>').text(function() {
                if (data.es_arriendo) {
                    return "Arriendo";
                } else if (data.es_venta) {
                    return "Venta";
                }
            }))
            .append($('<td>').text(function() {
                var formatoChile = {
                    style: 'currency',
                    currency: 'CLP'
                };
                return data.valor_propiedad.toLocaleString('es-CL', formatoChile);
            }))
            .append($('<td>').text(data.nombre_comuna))
            .append($('<td>').text(data.descripcion_estado))
            .append($('<td>').append(
                $('<a>')
                    .attr('href', '#')
                    .attr('onclick', 'cargarModalBase(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-bs-toggle', 'modal')
                    .attr('data-bs-target', '#PropiedadModalView')
                    .addClass('ModalPendienteView')
                    .append($('<i>')
                        .addClass('fa-solid fa-eye')
                        .attr('aria-hidden', 'true')
                    ),
                agregarBotones ? $('<a>')
                    .attr('href', '#')
                    .attr('onclick', 'cargarModalBase(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-bs-toggle', 'modal')
                    .attr('data-bs-target', '#PropiedadModalView')
                    .addClass('ModalPendienteView')
                    .append($('<i>')
                        .addClass('fa-solid fa-circle-check ms-2')
                        .css('color', '#369151')
                        .attr('aria-hidden', 'true')
                    ) : null,
                agregarBotones ? $('<a>')
                    .attr('href', '#')
                    .attr('onclick', 'cargarModalBase(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-bs-toggle', 'modal')
                    .attr('data-bs-target', '#PropiedadModalView')
                    .addClass('ModalPendienteView')
                    .append($('<i>')
                        .addClass('fa-solid fa-circle-xmark ms-2')
                        .css('color', '#c72929')
                        .attr('aria-hidden', 'true')
                    ) : null
            ))
            
    );
}

function API () {
    this.devolverPropPendientesAdmin = function (endpoint, datos) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : datos,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                cargarTablas(response, $('#admPropPendientes'), true);
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.devolverPropBaseAdmin = function (endpoint, datos) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : datos,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                cargarTablas(response, $('#admPropBase'), false);
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }
}