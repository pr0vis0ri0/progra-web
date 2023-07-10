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
var ep_detalle_prop_adm = "detalle_prop_adm/"
var access = localStorage.getItem('access_token')
var decodedToken = jwt_decode(access)
var api = new API()

$(document).ready(function (){
    api.devolverPropPendientesAdmin(url_api + ep_prop_pendiente_admin, devolverIdUsuario())
    api.devolverPropBaseAdmin(url_api + ep_prop_base_admin, devolverIdUsuario())
})

$('#btnViewValidar').click(function() {
    let id_usuario = decodedToken['id_usuario']
    let id_propiedad = $(this).attr('data-id')
    let ultimo_estado = 2
    let observacion_denegacion = $('#motivoDenegacion').val()
    datos = {
        id_usuario : id_usuario,
        id_propiedad : id_propiedad,
        ultimo_estado : ultimo_estado,
        observacion_denegacion : observacion_denegacion
    }
    api.actualizarPropiedad(url_api + ep_detalle_prop_adm, JSON.stringify(datos))
})

$('#btnViewDenegar').click(function() {
    let id_usuario = decodedToken['id_usuario']
    let id_propiedad = $(this).attr('data-id')
    let ultimo_estado = 3
    let observacion_denegacion = $('#motivoDenegacion').val()
    datos = {
        id_usuario : id_usuario,
        id_propiedad : id_propiedad,
        ultimo_estado : ultimo_estado,
        observacion_denegacion : observacion_denegacion
    }
    api.actualizarPropiedad(url_api + ep_detalle_prop_adm, JSON.stringify(datos))
    limpiarMotivo()
})

function cargarModal(id_propiedad) {
    var button = $(event.target).closest('a')
    var action = button.data('action')
    datos = {
        id_usuario : decodedToken['id_usuario'],
        id_propiedad : id_propiedad
    }
    api.devolverDetallePropiedad(url_api + ep_detalle_prop_adm, JSON.stringify(datos), action)
}

function checkActionModal(response, action) {
    cargarInformacionModal(response)
    switch (action) {
        case 'view':
            $('#btnViewValidar').attr('hidden','hidden')
            $('#btnViewDenegar').attr('hidden','hidden')
            // $('#denegacion-tab').removeAttr('hidden')
            // $('#motivoDenegacion').attr('disabled', 'disabled')
            $('#denegacion-tab').attr('hidden','hidden')
            $('#motivoDenegacion').attr('disabled', 'disabled')
            break;
        case 'check':
            $('#btnViewDenegar').attr('hidden','hidden')
            $('#btnViewValidar').removeAttr('hidden')
            $('#denegacion-tab').attr('hidden','hidden')
            $('#motivoDenegacion').attr('disabled', 'disabled')
            break;
        case 'deny':
            $('#btnViewValidar').attr('hidden','hidden')
            $('#btnViewDenegar').removeAttr('hidden')
            $('#denegacion-tab').removeAttr('hidden')
            $('#motivoDenegacion').removeAttr('disabled')
            $(document).on("click blur change focusout select", "#motivoDenegacion",
                function () {
                  checkMotivo();
                });
            break;
    }
}

function checkMotivo() {
    var error = 0
    if ($('#motivoDenegacion').val() == '') {
        error = 1;
        $('#motivoDenegacion').addClass('is-invalid')
    } else {
        $('#motivoDenegacion').removeClass('is-invalid')
        $('#motivoDenegacion').addClass('is-valid')
    }

    if (error == 1) {
        $('#btnViewDenegar').addClass('disabled')
                            .prop("disabled", true)
                            .each(function() {
                                this.style.pointerEvents = "none"
                            })
    } else {
        $('#btnViewDenegar').removeClass('disabled')
                            .prop("disabled", false)
                            .each(function() {
                                this.style.pointerEvents = "auto"
                            })
    }
}

function limpiarMotivo () {
    $('#motivoDenegacion').val('')
    $('#motivoDenegacion').removeClass('is-invalid')
    $('#motivoDenegacion').removeClass('is-valid')
    $('#btnViewDenegar').removeClass('disabled')
                            .prop("disabled", false)
                            .each(function() {
                                this.style.pointerEvents = "auto"
                            })
}

function cargarInformacionModal(i){
    $('#viewTituloModal').empty()
    $('#viewTituloModal').append($('<b>').text('Visualización Propiedad ' + i.id_propiedad))
    $('#viewNombrePropietario').val(i.nombre_usuario)
    $('#viewEstadoPropiedad').val(i.descripcion_estado)
    $('#viewValorPropiedad').val(i.valor_propiedad)
    $('#viewTipoPropiedad').val(i.nombre_tipo_propiedad)
    $('#viewRegion').val(i.nombre_region)
    $('#viewComuna').val(i.nombre_comuna)
    if (i.es_arriendo) { 
        $('#viewArriendoCheck').prop('checked', true);
        $('#viewVentaCheck').prop('checked', false);
    } else if (i.es_venta) {
        $('#viewVentaCheck').prop('checked', true);
        $('#viewArriendoCheck').prop('checked', false);
    }
    $('#viewMetrosTotales').val(i.metros_totales)
    $('#viewMetrosUtiles').val(i.metros_utiles)
    $('#viewCantidadDormitorios').val(i.cant_dormitorios)
    $('#viewCantidadBanos').val(i.cant_banos)
    if (i.permite_mascotas) {
        $('#viewCheckMascotas').prop('checked', true);
    } else {
        $('#viewCheckMascotas').prop('checked', false);
    }
    if (i.tiene_bodega) {
        $('#viewCheckBodega').prop('checked', true);
    } else {
        $('#viewCheckBodega').prop('checked', false);
    }
    if (i.tiene_estacionamiento) {
        $('#viewCheckEstacionamiento').prop('checked', true);
    } else {
        $('#viewCheckEstacionamiento').prop('checked', false);
    }
    $('#btnViewValidar').attr('data-id', i.id_propiedad)
    $('#btnViewDenegar').attr('data-id', i.id_propiedad)
}

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
                    .attr('onclick', 'cargarModal(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-action', 'view')
                    .attr('data-bs-toggle', 'modal')
                    .attr('data-bs-target', '#PropiedadModalView')
                    .addClass('ModalPendienteView')
                    .append($('<i>')
                        .addClass('fa-solid fa-eye')
                        .attr('aria-hidden', 'true')
                    ),
                agregarBotones ? $('<a>')
                    .attr('href', '#')
                    .attr('onclick', 'cargarModal(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-action', 'check')
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
                    .attr('onclick', 'cargarModal(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-action', 'deny')
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
                console.log(errorMessage);
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
                console.log(errorMessage);
            }
        })
    }

    this.devolverDetallePropiedad = function (endpoint, datos, action) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : datos,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                checkActionModal(response, action);
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                console.log(errorMessage);
            }
        })
    }

    this.actualizarPropiedad = function (endpoint, datos) {
        $.ajax({
            type : "PUT",
            url : endpoint,
            data : datos,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                location.reload()
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                console.log(errorMessage);
            }
        })
    }
}