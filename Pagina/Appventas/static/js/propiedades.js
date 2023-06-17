var funciones = new Propiedades()
var url_api = "http://localhost:9000/"
var ep_region = "region/";
var ep_filtro_comuna = "comuna/filtroRegiones/"
var ep_lista_propiedades = "lista_propiedades/"
var ep_filtro_propiedades = "propiedades_filtradas/"

$(document).ready(function () {

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

    funciones.devolverPropiedades(url_api + ep_lista_propiedades)

});

$(document).on('click', '.btn-acceso', function() {
    var idPropiedad = $(this).data('id');
    var propiedadURL = "http://localhost:8000/app/caracteristicas/id_propiedad".replace('id_propiedad',idPropiedad)
    window.location.href = propiedadURL;
});

$(document).on("click blur change focusout select", 
                "#select-regiones, #select-comunas, #valorDesde, #valorHasta, #arriendoCheck, #ventaCheck",
    function () {
        checkFiltros();
    }
);

$('#btnFiltrarPropiedades').click(function () {
    let datosFiltros = devolverDatosFiltros()
    funciones.filtrarPropiedades(url_api + ep_filtro_propiedades, datosFiltros)
})

function cargarHTML (response) {
    $('#lista-departamentos').empty()
    $('#container-nav').empty()
    // Número de propiedades que irán por página
    const propiedadesPorPagina = 10;
    console.log("1. " + propiedadesPorPagina);
    // Número total de propiedades que se obtiene desde el response
    var totalPropiedades
    if (Array.isArray(response)) {
        totalPropiedades = response.length
    } else {
        let data = new Array()
        data.push(response)
        totalPropiedades = data.length
    }
    // const totalPropiedades = response.length; // 50
    console.log("2. " + totalPropiedades);
    const paginasTotales = Math.ceil(totalPropiedades / propiedadesPorPagina);
    console.log("3. " + paginasTotales)
    // Obtener el número de la página actual (en caso de que se pase como parámetro en la URL)
    const pagActual = getParameterByName("page") || 1; // Si entras sin parámetro por defecto será la primera
    console.log("4. " + pagActual)
    // Aquí se calcularán el indicio inicial y final de las propiedades a mostrar
    const startIndex = (pagActual - 1) * propiedadesPorPagina;
    console.log("5. " + startIndex);
    const endIndex = startIndex + propiedadesPorPagina;
    console.log("6. " + endIndex);
    // Obtienes las propiedades de la página actual
    var datosPropiedad
    if (Array.isArray(response)) {
        datosPropiedad = response.slice(startIndex, endIndex);
    } else {
        datosPropiedad = [response]
    }
    console.log("7. " + datosPropiedad);
    $.each(datosPropiedad, function (i) {
        let divCol = $('<div></div>').addClass('col-md-6 mb-5');
        let card = $('<div></div>').addClass('card');
        let cardHeader = $('<div></div>').addClass('card-header')
        let textoRegion = $('<p></p>').addClass('card-text text-muted').text(datosPropiedad[i].nombre_region)
        let img = $('<img>').addClass('card-img-bottom');
        let cardBody = $('<div></div>').addClass('card-body');
        let cardTitle = $('<h5></h5>')
                            .addClass('card-title')
                            .html(datosPropiedad[i].nombre_tipo_propiedad);
        let cardSubtitle = $('<h6></h6>')
                            .addClass('card-subtitle mb-2 text-muted')
                            .html(datosPropiedad[i].nombre_comuna);
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
        card.append(cardHeader)
        cardHeader.append(textoRegion)
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

function devolverDatosFiltros () {
    datos = {
        id_comuna : parseInt($('#select-comunas').val()),
        valor_desde : parseInt($('#valorDesde').val()),
        valor_hasta : parseInt($('#valorHasta').val()),
        es_arriendo : $('#arriendoCheck').is(':checked'),
        es_venta : $('#ventaCheck').is(':checked'),
    }
    return JSON.stringify(datos);
}

function checkFiltros() {
    var error = 0

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

    if (parseInt($('#valorDesde').val()) > parseInt($('#valorHasta').val())) {
        $('#valorDesde').addClass('is-invalid')
        error = 1
    } else {
        $('#valorDesde').removeClass('is-invalid')
        $('#valorDesde').addClass('is-valid')
    }
    
    if (parseInt($('#valorHasta').val()) < parseInt($('#valorDesde').val())) {
        $('#valorHasta').addClass('is-invalid')
        error = 1
    } else {
        $('#valorHasta').removeClass('is-invalid')
        $('#valorHasta').addClass('is-valid')
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

    if (error == 1) {
        $('#btnFiltrarPropiedades').addClass('disabled')
                            .prop("disabled", true)
                            .each(function() {
                                this.style.pointerEvents = "none"
                            })
    } else {
        $('#btnFiltrarPropiedades').removeClass('disabled')
                            .prop("disabled", false)
                            .each(function() {
                                this.style.pointerEvents = "auto"
                            })
    }
}

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

function Propiedades () {
    this.devolverPropiedades = function (url) {
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            success: function (response) {
                cargarHTML(response)
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        });
    }
    this.filtrarPropiedades = function (url, data) {
        $.ajax({
            type : "POST",
            url : url,
            data : data,
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                console.log(response)
                cargarHTML(response)
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    
}