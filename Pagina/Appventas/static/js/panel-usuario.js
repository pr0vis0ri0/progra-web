if (!localStorage.getItem("access_token")) {
    window.location.href = "/app/login";
} else {
    let prior_ingreso = localStorage.getItem('access_token');
    let decodedPrior = jwt_decode(prior_ingreso)
    
    if (decodedPrior['id_perfil'] == 1) {
        window.location.href = "/app/administrador";
    }
}

var url_api = "http://localhost:9000/"
var ep_region = "region/";
var ep_filtro_comuna = "comuna/filtroRegiones/"
var ep_registro_propiedad = "registro_propiedad/"
var ep_propiedades_pendientes = "propiedades_pendientes/"
var ep_propiedades_validadas = "propiedades_validadas/"
var ep_detalle_propiedad_pendiente = "detalle_propiedad_pendiente/"
var ep_detalle_propiedad_validada = "detalle_propiedad_validada/"
var access = localStorage.getItem('access_token');
var decodedToken = jwt_decode(access)
var panel = new PanelUsuario()

// Aquí debe ir la carga de las propiedades pendientes del usuario.
$(document).ready(function (){
    panel.devolverPropiedadesPendientes(url_api + ep_propiedades_pendientes, devolverIdUsuario())
    panel.devolverPropiedadesBase(url_api + ep_propiedades_validadas, devolverIdUsuario())
})
// Aquí debe ir la carga de todas las propiedades del usuario.

// Validación para cuando se abra el modal.

$('#btnRegPropiedad').click(function (){
    let datosFormulario = devolverDatos()
    panel.registrarPropiedad(url_api + ep_registro_propiedad, datosFormulario)
});

$('#btnRedirigirModal').click(function (){
    panel.devolverRegiones(url_api + ep_region)

    $('#select-regiones').change(function (){
        let regionId = $(this).val();
        panel.devolverComunasRegion(url_api + ep_filtro_comuna + regionId)
    })
});

$('#btnCerrarModal').click(function (){
    limpiarFormulario()
});

// Validación para el formulario de registro de propiedad.

$(document).on("click blur change focusout select", 
                "#valorPropiedad, #tipoPropiedad, #select-regiones, #select-comunas, #arriendoCheck, #ventaCheck, #metrosTotales, #metrosUtiles, #cantidadDormitorios, #cantidadBanos",
    function () {
      checkFormulario();
    }
);

function cargarModal(id_propiedad) {
    datos = {
        id_usuario : decodedToken['id_usuario'],
        id_propiedad : id_propiedad
    }
    panel.devolverDetallePropiedadPendiente(url_api + ep_detalle_propiedad_pendiente, JSON.stringify(datos))
}

function cargarModalBase(id_propiedad) {
    datos = {
        id_usuario : decodedToken['id_usuario'],
        id_propiedad : id_propiedad
    }
    panel.devolverDetallePropiedadValidada(url_api + ep_detalle_propiedad_validada, JSON.stringify(datos))
}

function cargarInformacionModal(i){
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
}

function devolverIdUsuario () {
    data = {
        id_usuario : decodedToken['id_usuario']
    }
    return JSON.stringify(data)
}

function devolverDatos () {
    datos = {
        id_usuario : decodedToken['id_usuario'],
        valor_propiedad : parseInt($('#valorPropiedad').val()),
        es_arriendo : $('#arriendoCheck').is(':checked'),
        es_venta : $('#ventaCheck').is(':checked'),
        id_tipo_propiedad : parseInt($('#tipoPropiedad').val()),
        id_comuna : parseInt($('#select-comunas').val()),
        metros_totales : parseInt($('#metrosTotales').val()),
        metros_utiles : parseInt($('#metrosUtiles').val()),
        cant_dormitorios : parseInt($('#cantidadDormitorios').val()),
        cant_banos : parseInt($('#cantidadBanos').val()),
        permite_mascotas : $('#checkMascotas').is(':checked'),
        tiene_bodega : $('#checkBodega').is(':checked'),
        tiene_estacionamiento : $('#checkEstacionamiento').is(':checked')
    }
    return JSON.stringify(datos);
}

function checkFormulario () {
    var error = 0

    if ($('#valorPropiedad').val() == "") {
        $('#valorPropiedad').addClass('is-invalid')
        error = 1
    } else if (parseInt($('#valorPropiedad').val()) == 0) {
        $('#valorPropiedad').addClass('is-invalid')
        error = 1
    } else {
        $('#valorPropiedad').removeClass('is-invalid')
        $('#valorPropiedad').addClass('is-valid')        
    }

    if ($('#tipoPropiedad').val() == 0){
        $('#tipoPropiedad').addClass('is-invalid')
        error = 1
    } else {
        $('#tipoPropiedad').removeClass('is-invalid')
        $('#tipoPropiedad').addClass('is-valid')
    }

    if($('#select-regiones').val() == 0) {
        $('#select-regiones').addClass('is-invalid')
        error = 1
    } else {
        $('#select-regiones').removeClass('is-invalid')
        $('#select-regiones').addClass('is-valid')
    }

    if($('#select-comunas').val() == 0) {
        $('#select-comunas').addClass('is-invalid')
        error = 1
    } else {
        $('#select-comunas').removeClass('is-invalid')
        $('#select-comunas').addClass('is-valid')
    }

    if (!$('#arriendoCheck').is(':checked') && !$('#ventaCheck').is(':checked')) {
        $('#arriendoCheck').addClass('is-invalid')
        $('#ventaCheck').addClass('is-invalid')
        error = 1
    } else {
        $('#arriendoCheck').removeClass('is-invalid')
        $('#ventaCheck').removeClass('is-invalid')
        if($('#arriendoCheck').is(':checked')) {
            $('#arriendoCheck').addClass('is-valid')
        } else if ($('#ventaCheck').is(':checked')) {
            $('#ventaCheck').addClass('is-valid')
        }
    }

    if ($('#metrosTotales').val() == "") {
        $('#metrosTotales').addClass('is-invalid')
        error = 1
    } else if (parseInt($('#metrosTotales').val()) == 0) {
        $('#metrosTotales').addClass('is-invalid')
        error = 1
    } else if (parseInt($('#metrosTotales').val()) > parseInt($('#metrosUtiles').val())) {
        $('#metrosTotales').addClass('is-invalid')        
    } else {
        $('#metrosTotales').removeClass('is-invalid')
        $('#metrosTotales').addClass('is-valid')   
    }

    if ($('#metrosUtiles').val() == "") {
        $('#metrosUtiles').addClass('is-invalid')
        error = 1
    } else if (parseInt($('#metrosUtiles').val()) == 0) {
        $('#metrosUtiles').addClass('is-invalid')
        error = 1
    } else if (parseInt($('#metrosUtiles').val()) < parseInt($('#metrosTotales').val())) {
        $('#metrosUtiles').addClass('is-invalid') 
    } else {
        $('#metrosUtiles').removeClass('is-invalid')
        $('#metrosUtiles').addClass('is-valid')  
    }

    if ($('#cantidadDormitorios').val() == "") {
        $('#cantidadDormitorios').addClass('is-invalid')
        error = 1
    } else {
        $('#cantidadDormitorios').removeClass('is-invalid')
        $('#cantidadDormitorios').addClass('is-valid')        
    }

    if ($('#cantidadBanos').val() == "") {
        $('#cantidadBanos').addClass('is-invalid')
        error = 1
    } else {
        $('#cantidadBanos').removeClass('is-invalid')
        $('#cantidadBanos').addClass('is-valid')        
    }

    if (error == 1) {
        $('#btnRegPropiedad').addClass('disabled')
                            .prop("disabled", true)
                            .each(function() {
                                this.style.pointerEvents = "none"
                            })
    } else {
        $('#btnRegPropiedad').removeClass('disabled')
                            .prop("disabled", false)
                            .each(function() {
                                this.style.pointerEvents = "auto"
                            })
    }
}

function limpiarFormulario () {
    $('#valorPropiedad').val("")
    $('#tipoPropiedad').val(0)
    $('#select-regiones').val(0)
    $('#select-comunas').val(0)
    $('#arriendoCheck').prop('checked', false)
    $('#ventaCheck').prop('checked', false)
    $('#metrosTotales').val("")
    $('#metrosUtiles').val("")
    $('#cantidadDormitorios').val("")
    $('#cantidadBanos').val("")
    $('#checkMascotas').prop('checked', false)
    $('#checkBodega').prop('checked', false)
    $('#checkEstacionamiento').prop('checked', false)
    $('#valorPropiedad').removeClass('is-valid is-invalid')
    $('#tipoPropiedad').removeClass('is-valid is-invalid')
    $('#select-regiones').removeClass('is-valid is-invalid')
    $('#select-comunas').removeClass('is-valid is-invalid')
    $('#arriendoCheck').removeClass('is-valid is-invalid')
    $('#ventaCheck').removeClass('is-valid is-invalid')
    $('#metrosTotales').removeClass('is-valid is-invalid')
    $('#metrosUtiles').removeClass('is-valid is-invalid')
    $('#cantidadDormitorios').removeClass('is-valid is-invalid')
    $('#cantidadBanos').removeClass('is-valid is-invalid')
    $('#btnRegPropiedad').addClass('disabled')
}

// function cargarTablaPendientes(p) {
//     $.each(p, function (i){
//         $("#propiedadesPendientes")
//         .append($('<tr>')
//             .append($('<td>')
//                 .text(p[i].id_propiedad)
//             )
//             .append($('<td>')
//                 .text(p[i].nombre_tipo_propiedad)
//             )
//             .append($('<td>')
//                 .text(function (){
//                     if (p[i].es_arriendo) {
//                         return "Arriendo"
//                     } else if (p[i].es_venta) {
//                         return "Venta"
//                     }
//                 })
//             )
//             .append($('<td>')
//                 .text(function (){
//                     var formatoChile = {
//                         style : 'currency',
//                         currency : 'CLP'
//                     }
//                     return p[i].valor_propiedad.toLocaleString('es-CL', formatoChile)
//                 })
//             )
//             .append($('<td>')
//                 .text(p[i].nombre_comuna)
//             )
//             .append($('<td>')
//                 .append($('<a>')
//                     .attr('href', '#')
//                     .attr('onclick', 'cargarModal(' + p[i].id_propiedad + ')')
//                     .attr('data-id', p[i].id_propiedad)
//                     .attr('data-bs-toggle', 'modal')
//                     .attr('data-bs-target', '#PropiedadModalView')
//                     .addClass('ModalPendienteView')
//                     .append($('<i>')
//                         .addClass('fa fa-eye')
//                         .attr('aria-hidden', 'true')
//                     )
//                 )
//             )
//         );
//     })
// }

function cargarTablaPendientes(p) {
    if (Array.isArray(p)) {
        $.each(p, function(i) {
            appendTableRowPendientes(p[i]);
        });
    } else {
        appendTableRowPendientes(p);
    }
}

function appendTableRowPendientes(data) {
    $("#propiedadesPendientes").append(
        $('<tr>')
            .append($('<td>').text(data.id_propiedad))
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
            .append($('<td>').append(
                $('<a>')
                    .attr('href', '#')
                    .attr('onclick', 'cargarModal(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-bs-toggle', 'modal')
                    .attr('data-bs-target', '#PropiedadModalView')
                    .addClass('ModalPendienteView')
                    .append($('<i>')
                        .addClass('fa fa-eye')
                        .attr('aria-hidden', 'true')
                    )
            ))
    );
}

function cargarTablaBase(p) {
    if (Array.isArray(p)) {
        $.each(p, function(i) {
            appendTableRowBase(p[i]);
        });
    } else {
        appendTableRowBase(p);
    }
}

function appendTableRowBase(data) {
    $("#basePropiedades").append(
        $('<tr>')
            .append($('<td>').text(data.id_propiedad))
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
            .append($('<td>').append(
                $('<a>')
                    .attr('href', '#')
                    .attr('onclick', 'cargarModalBase(' + data.id_propiedad + ')')
                    .attr('data-id', data.id_propiedad)
                    .attr('data-bs-toggle', 'modal')
                    .attr('data-bs-target', '#PropiedadModalView')
                    .addClass('ModalPendienteView')
                    .append($('<i>')
                        .addClass('fa fa-eye')
                        .attr('aria-hidden', 'true')
                    )
            ))
    );
}

function PanelUsuario () {
    this.registrarPropiedad = function (endpoint, data_propiedad) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : data_propiedad,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                $('#modalRegistro').modal('toggle')
                location.reload()
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.devolverDetallePropiedadPendiente = function (endpoint, datos) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : datos,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                cargarInformacionModal(response)
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.devolverDetallePropiedadValidada = function (endpoint, datos) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : datos,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                cargarInformacionModal(response)
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.devolverPropiedadesPendientes = function (endpoint, id_usuario) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : id_usuario,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                if (!response.hasOwnProperty('mensaje-error')) {
                    cargarTablaPendientes(response);
                }
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.devolverPropiedadesBase = function (endpoint, id_usuario) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : id_usuario,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                if (!response.hasOwnProperty('mensaje-error')) {
                    cargarTablaBase(response);
                }
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.devolverRegiones = function (endpoint) {
        $.ajax({
            url: endpoint,
            type: "GET",
            dataType: "json",
            success: function (regiones) {
                $.each(regiones, function (i) {
                    let optionRegion = $('<option></option>')
                                    .attr({value : regiones[i].id_region})
                                    .html(regiones[i].nombre_region);
                    $('#select-regiones').append(optionRegion);
                });
            }
        });    
    }

    this.devolverComunasRegion = function (endpoint) {
        $.ajax({
            url: endpoint + "/",
            type: "POST",
            dataType: "json",
            success: function(comunas){
                $('#select-comunas').empty();
                let optionDefault = $('<option></option>')
                                    .attr({value : 0})
                                    .html('Escoge Comuna')
                $('#select-comunas').append(optionDefault)
                $.each(comunas, function (i){
                    let optionComuna = $('<option></option>')
                                        .attr({value : comunas[i].id_comuna})
                                        .html(comunas[i].nombre_comuna);
                    $('#select-comunas').append(optionComuna)
                })
            }
        })
    }
}