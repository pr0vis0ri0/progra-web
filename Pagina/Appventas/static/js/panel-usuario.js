if (!localStorage.getItem("access_token")) {
    window.location.href = "/app/login";
}


// Aquí debe ir la carga de las propiedades pendientes del usuario.

// Aquí debe ir la carga de todas las propiedades del usuario.


var url_api = "http://localhost:9000/"
var ep_region = "region/";
var ep_filtro_comuna = "comuna/filtroRegiones/"
var ep_registro_propiedad = "registro_propiedad/"
var access = localStorage.getItem('access_token');
var decodedToken = jwt_decode(access)

// Validación para cuando se abra el modal.

$('#btnRegPropiedad').click(function (){
    let datosFormulario = devolverDatos()
    let panel = new PanelUsuario()
    panel.registrarPropiedad(url_api + ep_registro_propiedad, datosFormulario)
});

$('#btnRedirigirModal').click(function (){
    let panel = new PanelUsuario()
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

function devolverDatos () {
    datos = {
        id_usuario : decodedToken['user_id'],
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

function PanelUsuario () {
    this.registrarPropiedad = function (ep_registro_propiedad, data_propiedad) {
        $.ajax({
            type : "POST",
            url : ep_registro_propiedad,
            data : data_propiedad,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                alert('Se logró grabar la propiedad.')
                $('#modalRegistro').modal('toggle')
                limpiarFormulario()
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.devolverPropiedadesPendientes = function (endpoint) {
        $.ajax({
            type : "POST",
            url : ep_registro_propiedad,
            data : data_propiedad,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                alert('Se logró grabar la propiedad.')
                $('#modalRegistro').modal('toggle')
                limpiarFormulario()
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