$(document).ready(function () {
    $("#categoriaLoja").select2({
        tags: true,
        width: '100%',
        theme: "classic"
    });

    getAllCategories().then((categorias) => {
        console.log(categorias)
        options = ''
        categorias.forEach(categoria => {
            options = options + '<option value="'+categoria+'">'+categoria+'</option>'
        });
        $("#categoriaLoja").append(options)
    })

    $('#cpfCliente').on('input', function() {
        var cpf = $(this).val().replace(/\D/g, ''); // Remove todos os caracteres não numéricos

        if (cpf.length === 11 && /^\d{11}$/.test(cpf)) {
          // CPF válido
          $(this).removeClass('is-invalid').addClass('is-valid');
        } else {
          // CPF inválido
          $(this).removeClass('is-valid').addClass('is-invalid');
        }
    });

    $('.inputLogin').on('input', function() {
        login = $(this).val()
        validarLogin(login).then((novoLogin) => {
            if(novoLogin == login){
                $(this).removeClass('is-invalid').addClass('is-valid');
            } else{
                $(this).removeClass('is-valid').addClass('is-invalid');
            }
        })
    });

    $(".cadastrarBtn").click(function (e) { 
        e.preventDefault()
        type = $(this).attr("data-type")
        if(type == "cliente"){
            cliente = {}
            cliente["nome"] = $("#nomeCliente").val()
            cliente["cpf"] = $("#cpfCliente").val()
            cliente["login"] = $("#loginCliente").val()
            cliente["senha"] = $("#senhaCliente").val()
            cadastrarCliente(cliente).then((data) => {
                if(data["cadastro"] == "success"){
                    let timerInterval
                    Swal.fire({
                        title: 'Cliente cadastrado!',
                        timer: 2000,
                        timerProgressBar: true,
                        willClose: () => {
                            clearInterval(timerInterval)
                        }
                    }).then((result) => {
                        window.location.href = "login.html"
                    })
                }
            })
        } else{
            loja = {}
            loja["nome"] = $("#nomeLoja").val()
            loja["categoria"] = $("#categoriaLoja").val()
            endereco = {}
            endereco["cidade"] = $("#inputCidade").val()
            endereco["bairro"] = $("#inputBairro").val()
            endereco["rua"] = $("#inputRua").val()
            endereco["num"] = $("#inputNum").val()
            endereco["complemento"] = $("#inputComplemento").val()
            endereco["cep"] = $("#inputCEP").val()
            loja["endereco"] = endereco
            loja["login"] = $("#loginLoja").val()
            loja["senha"] = $("#senhaLoja").val()
            cadastrarLoja(loja).then((data) => {
                if(data["cadastro"] == "success"){
                    let timerInterval
                    Swal.fire({
                        title: 'Loja cadastrada!',
                        timer: 2000,
                        timerProgressBar: true,
                        willClose: () => {
                            clearInterval(timerInterval)
                        }
                    }).then((result) => {
                        window.location.href = "login.html"
                    })
                }
            })
        }
    });

    $('input[name="type"]').change(function (e) { 
        var type = ($(this).val() == "Cliente") ? "Loja" : "Cliente";
        $("#cadastro"+type).addClass("d-none");
        $("#cadastro"+$(this).val()).removeClass("d-none");
    });
});

async function validarLogin(login) {
    novoLogin = await eel.validarNovoLogin(login)()
    return novoLogin
}

async function cadastrarCliente(cliente){
    return await eel.cadastrarCliente(cliente)()
}

async function cadastrarLoja(loja){
    return await eel.cadastrarLoja(loja)()
}

async function getAllCategories(){
    return await eel.getAllCategories()()
}