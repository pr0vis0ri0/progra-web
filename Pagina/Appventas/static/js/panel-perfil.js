if (!localStorage.getItem("access_token")) {
    window.location.href = "/app/login";
}

var url_api = "http://localhost:9000/"
var perfil_usuario = "perfil_usuario/"
var access = localStorage.getItem('access_token')
var decodedToken = jwt_decode(access)
var api = new API()

$(document).ready(function() {
    id_perfil = decodedToken['id_perfil']
    if (id_perfil == 1) {
        $('#botonesVista').append(
                $('<button>')
                    .addClass('btn btn-primary')
                    .attr('id', 'btnVolverAdmin')
                    .attr('type', 'button')
                    .text('Volver'),
                $('<button>')
                    .addClass('btn btn-primary')
                    .attr('id', 'btnActualizarPerfil')
                    .attr('type', 'button')
                    .text('Grabar')
        )
    } else {
        $('#botonesVista').append(
            $('<button>')
                .addClass('btn btn-primary')
                .attr('id', 'btnVolverUsuario')
                .attr('type', 'button')
                .text('Volver'),
            $('<button>')
                .addClass('btn btn-primary')
                .attr('id', 'btnActualizarPerfil')
                .attr('type', 'button')
                .text('Grabar')
    )
    }
    $('#userRUT').inputmask()
    $("#userFNacimiento").inputmask()
    api.devolverDatosUsuario(url_api + perfil_usuario, devolverIdUsuario())

    $('#btnVolverUsuario').click(function() {
        window.location.href = "/app/usuario"
    })
    
    $('#btnVolverAdmin').click(function() {
        window.location.href = "/app/administrador"
    })
    
    $('#btnActualizarPerfil').click(function() {
        api.actualizarDatosUsuario(url_api + perfil_usuario, devolverDataUsuario())
    })
    
})

$($('#userRUT')).rut();

$("input#userRUT").rut({
	formatOn: 'keyup',
    minimumLength: 8, // validar largo mínimo; default: 2
	validateOn: 'change' // si no se quiere validar, pasar null
});

$("input#userRUT").rut().on('rutInvalido', function(e) {
    $('#userRUT').removeClass('is-valid')
	$('#userRUT').addClass('is-invalid')
});

$("input#userRUT").rut().on('rutValido', function(e) {
    $('#userRUT').removeClass('is-invalid')
	$('#userRUT').addClass('is-valid')
});

function devolverIdUsuario () {
    data = {
        id_usuario : decodedToken['id_usuario']
    }
    return JSON.stringify(data)
}

function devolverDataUsuario() {
    data = {
        id_usuario : decodedToken['id_usuario'],
        primer_nombre : $('#userPNombre').val(),
        segundo_nombre : $('#userSNombre').val(),
        apellido_paterno : $('#userAPaterno').val(),
        apellido_materno : $('#userAMaterno').val(),
        email : $('#userCorreo').val(),
        rut : $('#userRUT').val(),
        fecha_nacimiento : $('#userFNacimiento').val()
    }
    return JSON.stringify(data)
}

function cargarInformacionUsuario(i) {
    $('#userPNombre').val(i['primer_nombre'])
    $('#userSNombre').val(i['segundo_nombre'])
    $('#userAPaterno').val(i['apellido_paterno'])
    $('#userAMaterno').val(i['apellido_materno'])
    $('#userCorreo').val(i['email'])
    $('#userRUT').val(i['rut'])
    $('#userFNacimiento').val(i['fecha_nacimiento'])
}

function API () {
    this.devolverDatosUsuario = function (endpoint, datos) {
        $.ajax({
            type : "POST",
            url : endpoint,
            data : datos,
            headers: { "Authorization": 'Bearer ' + access },
            contentType: "application/json; charset=utf-8",
            dataType : "json",
            success : function (response) {
                cargarInformacionUsuario(response)
            },
            error : function (jqXHR, status, errorThrown) {
                var errorMessage = "Error: " + errorThrown;
                alert(errorMessage);
            }
        })
    }

    this.actualizarDatosUsuario = function (endpoint, datos) {
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
                alert(errorMessage);
            }
        })
    }
}