$(document).ready(function () {
    var url_api = "http://localhost:9000/"
    let ep_region = "region/";
    let ep_filtro_comuna = "comuna/filtroRegiones/"

    $.ajax({
        url: url_api + ep_region,
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

    $('#select-regiones').change(function (){
        let regionId = $(this).val();
        
        $.ajax({
            url: url_api + ep_filtro_comuna + regionId + "/",
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
    })
});

$(document).on("click blur change focusout select", 
                "#valorPropiedad, #tipoPropiedad, #select-regiones, #select-comunas",
    function () {
      checkFormulario();
    }
);

function checkFormulario () {
    var error = 0
    if ($('#valorPropiedad').val() == "") {
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
