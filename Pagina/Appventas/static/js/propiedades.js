// Ver propiedad debe tener un data-id="" con el id_propiedad, lo demás
// sólo lo muestra dinámicamente el sitio con la request de JQuery

$(document).ready(function () {
    $.ajax({
        url: "http://localhost:9000/api/v1/region/",
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
            url: "http://localhost:9000/api/v1/comuna/filtroRegiones/" + regionId + "/",
            type: "GET",
            dataType: "json",
            success: function(comunas){
                $('#select-comunas').empty();

                $.each(comunas, function (i){
                    let optionComuna = $('<option></option>')
                                        .attr({value : comunas[i].id_comuna})
                                        .html(comunas[i].nombre_comuna);
                    $('#select-comunas').append(optionComuna)
                })
            }
        })
    })

    $.ajax({
        url: "http://localhost:9000/api/v1/propiedad/",
        type: "GET",
        dataType: "json",
        success: function (propiedades) {
            $.each(propiedades, function (i) {
                let divCol = $('<div></div>').addClass('col-md-6 mb-5');
                let card = $('<div></div>').addClass('card');
                let img = $('<img>').addClass('card-img-top');
                let cardBody = $('<div></div>').addClass('card-body');
                let cardTitle = $('<h5></h5>').addClass('card-title');
                let cardSubtitle = $('<h6></h6>')
                                    .addClass('card-subtitle text-muted')
                                    .html('Pendiente');
                let cardText = $('<p></p>').addClass('card-text mt-3');
                let dFlex = $('<div></div>').addClass('d-flex justify-content-between');
                let txtStart = $('<h6></h6>').addClass('text-start');
                let txtEnd = $('<h6></h6>').addClass('text-end');
                let divEnd = $('<div></div>').addClass('text-end');
                let btnPropiedad = $('<a></a>')
                                    .addClass('btn btn-primary')
                                    .html('Ver propiedad');
                $('#lista-departamentos').append(divCol);
                divCol.append(card);
                if(propiedades[i].id_tipo_propiedad == 1) {
                    img.attr({
                        src : staticUrl + "departamentos/departamento-id-x.jpg",
                        alt : "Departamento"
                    })
                    cardTitle.html('Departamento');
                } else {
                    img.attr({
                        src : staticUrl + "casas/casa-id-x.jpg",
                        alt : 'Casa'
                    })
                    cardTitle.html('Casa');
                }
                card.append(img);
                card.append(cardBody);
                cardBody.append(cardTitle);
                cardBody.append(cardSubtitle);
                cardBody.append(cardText);
                cardText.append(dFlex);
                if(propiedades[i].es_arriendo != 0) {
                    txtStart.html('Arriendo');
                    dFlex.append(txtStart);
                } else if (propiedades[i].es_venta != 0) {
                    txtStart.html('Venta');
                    dFlex.append(txtStart);
                }
                dFlex.append(txtEnd.html("$" + propiedades[i].valor_propiedad));
                cardText.append('<hr>');
                cardBody.append(divEnd);
                divEnd.append(btnPropiedad.attr({
                    href : "#",
                    'data-id' : propiedades[i].id_propiedad
                }))
            });
        }
    });
});