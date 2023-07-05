$(document).on("click blur change focusout select", 
                "#nombre,#Email,#mensaje",
    function () {
      checkFormulario();
    }
);

function checkFormulario () {
    var error = 0

    if ($('#nombre').val() == "") {
        $('#nombre').addClass('is-invalid')
        error = 1
    } else {
        $('#nombre').removeClass('is-invalid')
        $('#nombre').addClass('is-valid')  
    }
    

    $('#email').change(function () {
            var status = false;
            var email = $('#email').val();
            var emailLength = email.length;
            if (email != "" && emailLength > 4) {
                email = email.replace(/\s/g, "");  //To remove space if available
                var atIndex = email.indexOf("@");

                if (atIndex > -1) {   //To check (.) and (@) present in the string
                    if ( atIndex != 0 && atIndex != emailLength && email.slice(email.length - 1) != ".") {   //To check (.) and (@) are not the firat or last character of string
                        
                        var atCount = email.split('@').length

                        if (atCount == 2 && (atIndex > 1)) { //To check (@) present multiple times or not in the string. And (.) and (@) not located subsequently
                            status = true;
                           
                        }
                    }
                }

            }

            $('#email').val(email);
            if (!status) {
                $('#email').addClass('is-invalid');
            }else{
                $('#email').removeClass('is-invalid')
                $('#email').addClass('is-valid')
            }
        });

        if ($('#mensaje').val() == "") {
            $('#mensaje').addClass('is-invalid')
            error = 1
        } else {
            $('#mensaje').removeClass('is-invalid')
            $('#mensaje').addClass('is-valid')  
        }
        
        if (error == 1) {
            $('#btn-esteban').addClass('disabled')
                                .prop("disabled", true)
                                .each(function() {
                                    this.style.pointerEvents = "none"
                                })
        } else {
            
            $('#btn-esteban').removeClass('disabled')
                                .prop("disabled", false)
                                .each(function() {
                                    this.style.pointerEvents = "auto"
                                })
        }

    }
    function botoni() {
        alert('Confirmar envio de formulario');
}