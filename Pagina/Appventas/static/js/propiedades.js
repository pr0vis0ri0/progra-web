$(document).ready(function () {
    
    $.ajax({
        url: "http://localhost:9000/region/",
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
            url: "http://localhost:9000/comuna/filtroRegiones/" + regionId + "/",
            type: "POST",
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
        url: "http://localhost:9000/detalle_propiedad/",
        type: "GET",
        dataType: "json",
        success: function (response) {
            // Número de propiedades que irán por página
            const propiedadesPorPagina = 10;
            // console.log("1. " + propiedadesPorPagina);
            // Número total de propiedades que se obtiene desde el response
            const totalPropiedades = response.length; // 50
            // console.log("2. " + totalPropiedades);
            const paginasTotales = Math.ceil(totalPropiedades / propiedadesPorPagina);
            // console.log("3. " + paginasTotales)
            // Obtener el número de la página actual (en caso de que se pase como parámetro en la URL)
            const pagActual = getParameterByName("page") || 1; // Si entras sin parámetro por defecto será la primera
            //console.log("4. " + pagActual)
            // Aquí se calcularán el indicio inicial y final de las propiedades a mostrar
            const startIndex = (pagActual - 1) * propiedadesPorPagina;
            //console.log("6. " + startIndex);
            const endIndex = startIndex + propiedadesPorPagina;
            //console.log("6. " + endIndex);
            // Obtienes las propiedades de la página actual
            const datosPropiedad = response.slice(startIndex, endIndex);
            //console.log("7. " + propiedades);

            $.each(datosPropiedad, function (i) {

                let divCol = $('<div></div>').addClass('col-md-6 mb-5');
                let card = $('<div></div>').addClass('card');
                let img = $('<img>').addClass('card-img-top');
                let cardBody = $('<div></div>').addClass('card-body');
                let cardTitle = $('<h5></h5>')
                                    .addClass('card-title')
                                    .html(datosPropiedad[i].nombre_tipo_propiedad);
                let cardSubtitle = $('<span></span>')
                                    .addClass('badge rounded-pill bg-success')
                                    .html(datosPropiedad[i].nombre_comuna + ", " + datosPropiedad[i].nombre_region);
                let cardText = $('<p></p>').addClass('card-text mt-3');
                let dFlex = $('<div></div>').addClass('d-flex justify-content-between');
                let txtStart = $('<h6></h6>').addClass('text-start');
                let txtEnd = $('<h6></h6>').addClass('text-end');
                let divEnd = $('<div></div>').addClass('text-end');
                let btnPropiedad = $('<a></a>')
                                    .addClass('btn btn-primary btn-acceso')
                                    .html('Ver propiedad');
                $('#lista-departamentos').append(divCol);
                divCol.append(card);


                if(datosPropiedad[i].nombre_tipo_propiedad == 'Departamento') {
                    img.attr({
                        src : staticUrl + "departamentos/departamento-id-x.jpg",
                        alt : "Departamento"
                    })
                } else {
                    img.attr({
                        src : staticUrl + "casas/casa-id-x.jpg",
                        alt : 'Casa'
                    })
                }

                card.append(img);
                card.append(cardBody);
                cardBody.append(cardTitle);
                cardBody.append(cardSubtitle);
                cardBody.append(cardText);
                cardText.append(dFlex);

                if(datosPropiedad[i].es_arriendo != 0) {
                    txtStart.text('Arriendo');
                    dFlex.append(txtStart);
                } else if (datosPropiedad[i].es_venta != 0) {
                    txtStart.text('Venta');
                    dFlex.append(txtStart);
                }

                var formatoChile = {
                    style : 'currency',
                    currency : 'CLP'
                }

                dFlex.append(txtEnd.html("$" + datosPropiedad[i].valor_propiedad.toLocaleString('es-CL'),formatoChile));
                cardText.append('<hr>');
                cardBody.append(divEnd);
                divEnd.append(btnPropiedad.attr({
                    href : "#",
                    'data-id' : datosPropiedad[i].id_propiedad
                }))
            });



            // Se genera el nav destinado para la páginación en el HTML
            // con las clases que están acá https://getbootstrap.com/docs/5.0/components/pagination/#alignment
            const paginacionContainer = $('<nav></nav>').addClass('mt-5').attr({ 'aria-label' : 'Navegación de páginas' });
            const paginacionLista = $('<ul></ul>').addClass('pagination justify-content-center');
            paginacionContainer.append(paginacionLista);

            // Creación de botones
            if (pagActual > 1) {
                paginacionLista.append(creacionBotonPaginacion('Anterior', parseInt(pagActual) - 1));
            }
            for (let i = 1; i <= paginasTotales; i++) {
                paginacionLista.append(creacionBotonPaginacion(i, i, parseInt(pagActual)));
            }
            if (pagActual < paginasTotales) {
                paginacionLista.append(creacionBotonPaginacion('Siguiente', parseInt(pagActual) + 1));
            }

            $('#container-nav').append(paginacionContainer);
        }
    });

    $(document).on('click', '.btn-acceso', function() {
        var idPropiedad = $(this).data('id');
        var propiedadURL = "http://localhost:8000/app/caracteristicas/id_propiedad".replace('id_propiedad',idPropiedad)
        window.location.href = propiedadURL;
      });

});

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    const regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)");
    const results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return "";
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function creacionBotonPaginacion(label, pageNumber, currentPage) {
  const listItem = $('<li></li>').addClass('page-item');
  const link = $('<a></a>').addClass('page-link').attr('href', '?page=' + pageNumber).text(label);
    if (currentPage === pageNumber) {
        listItem.addClass('active');
    } 
  listItem.append(link);
  return listItem;
}