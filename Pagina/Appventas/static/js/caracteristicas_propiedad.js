$(document).ready(function () {
    var url_api = "http://localhost:9000/"
    let endpoint_dp = "detalle_propiedad/";

    $.ajax({
        url: url_api + endpoint_dp + id_propiedad,
        type: "GET",
        dataType: "json",
        success: function (data) {
            $('.propiedad-locacion').html(data.nombre_comuna + ", " + data.nombre_region)

            if(data.nombre_tipo_propiedad == 'Departamento') {
                $('.propiedad-img').attr({
                    src : staticUrl + "departamentos/departamento-id-x.jpg",
                    alt : "Departamento"
                });
                $('.propiedad-tipo').html('Departamento');
                $('.motivacion-departamento').removeAttr('hidden');
            } else {
                $('.propiedad-img').attr({
                    src : staticUrl + "casas/casa-id-x.jpg",
                    alt : 'Casa'
                });
                $('.propiedad-tipo').html('Casa');
                $('.motivacion-casa').removeAttr('hidden');
            }

            if(data.es_arriendo != 0) {
                $('.propiedad-es').html('Arriendo');
            } else if (data.es_venta != 0) {
                $('.propiedad-es').html('Venta');
            }

            var formatoChile = {
                style : 'currency',
                currency : 'CLP'
            }
            $('.propiedad-valor').html(data.valor_propiedad.toLocaleString('es-CL', formatoChile))

            $('.car-1').append(' ' + data.metros_totales + ' m² totales');
            $('.car-2').append(' ' + data.metros_utiles + ' m² utiles');
            $('.car-3').append(' ' + data.cant_dormitorios + ' dormitorio/s');
            $('.car-4').append(' ' + data.cant_banos + ' baño/s');

            if (data.permite_mascotas != 0 ) {
                $('.car-5').append(' Permite mascotas');
            } else {
                $('.car-5').append(' No permite mascotas');
            }

            if (data.tiene_bodega != 0 ) {
                $('.car-6').append(' Tiene bodega');
            } else {
                $('.car-6').append(' No tiene bodega');
            }

            if (data.tiene_estacionamiento != 0 ) {
                $('.car-7').append(' Tiene estacionamiento');
            } else {
                $('.car-7').append(' No tiene estacionamiento');
            }

        }
    });
});