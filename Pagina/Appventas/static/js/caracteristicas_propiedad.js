$(document).ready(function () {

    $.ajax({
        url: "http://localhost:9000/detalle_propiedad/" + id_propiedad,
        type: "GET",
        dataType: "json",
        success: function (response) {
            var propiedad = response['data_propiedad']
            var caracteristicas = response['data_caracteristica']
            var comuna = response['data_comuna']
            var region = response['data_region']

            $('.propiedad-locacion').html(comuna.nombre_comuna + ", " + region.nombre_region)

            if(propiedad.id_tipo_propiedad == 1) {
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

            if(propiedad.es_arriendo != 0) {
                $('.propiedad-es').html('Arriendo');
            } else if (propiedad.es_venta != 0) {
                $('.propiedad-es').html('Venta');
            }

            var formatoChile = {
                style : 'currency',
                currency : 'CLP'
            }
            $('.propiedad-valor').html(propiedad.valor_propiedad.toLocaleString('es-CL', formatoChile))

            $('.car-1').append(' ' + caracteristicas.metros_totales + ' m² totales');
            $('.car-2').append(' ' + caracteristicas.metros_utiles + ' m² utiles');
            $('.car-3').append(' ' + caracteristicas.cant_dormitorios + ' dormitorio/s');
            $('.car-4').append(' ' + caracteristicas.cant_banos + ' baño/s');

            if (caracteristicas.permite_mascotas != 0 ) {
                $('.car-5').append(' Permite mascotas');
            } else {
                $('.car-5').append(' No permite mascotas');
            }

            if (caracteristicas.tiene_bodega != 0 ) {
                $('.car-6').append(' Tiene bodega');
            } else {
                $('.car-6').append(' No tiene bodega');
            }

            if (caracteristicas.tiene_estacionamiento != 0 ) {
                $('.car-7').append(' Tiene estacionamiento');
            } else {
                $('.car-7').append(' No tiene estacionamiento');
            }

        }
    });
});