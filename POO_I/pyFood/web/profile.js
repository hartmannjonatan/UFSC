let USER = null

$(document).ready(function() {
    $(".logout").click(function (e) { 
        logout().then(() =>  {
            window.close()
            window.location.href = "./login.html"
        })
    });

    $(".btnDeletarConta").click(function (e) { 
        e.preventDefault();
        Swal.fire({
            title: 'Você realmente deseja deletar sua conta?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sim',
            cancelButtonText: 'Cancelar'
          }).then((result) => {
            if (result.isConfirmed) {
                deleteUser().then((data) => {
                    if(data["delete"] == "success"){
                        let timerInterval
                        Swal.fire({
                            title: 'Conta deletada! Volte sempre!',
                            timer: 3000,
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
    });

    Swal.fire({
        title: "Carregando dados...",
        html: '<div class="loader"></div>',
        showConfirmButton: false,
        allowOutsideClick: false,
        willOpen: () => {
          Swal.showLoading();
        }
    });
    loadUser().then(() => {
        Swal.close();
        if(USER == null || USER == undefined || USER["error"] != undefined){
            window.location.href = "./login.html"
        }
        $("#not"+USER["type"]).remove();

        if(USER["type"] == "cliente"){
            $('#searchPedido').on('input', function() {
                var filtro = $(this).val().toLowerCase();
                
                // Filtrar os cards de pedidos
                $('#pedidos .card').hide().filter(function() {
                  var restaurante = $(this).find('.nomeRestaurante').text().toLowerCase();
                  return restaurante.includes(filtro);
                }).show();
            });
        
            $('#editarDadosPessoais').submit(function(event) {
                event.preventDefault(); // Evita o envio padrão do formulário
        
                var senha = $('#inputSenha').val()
                var nome = $('#inputNome').val()
                var cpf = $('#inputCPF').val()
                
                Swal.fire({
                    title: "Carregando...",
                    showConfirmButton: false,
                    allowOutsideClick: false,
                    willOpen: () => {
                      Swal.showLoading();
                    }
                });
                editProfileCliente(nome, cpf, USER["login"], senha).then(() => {
                    Swal.close();
                    Swal.fire('Alterações foram salvas!', '', 'success')
                    $('#modalEditarDados').modal('hide')
                    location.reload()
                })
            });

            $('h1').html("Olá "+USER["nome"]+"!");
            $('#nome').html(USER["nome"]);
            $('#cpf').html(USER["cpf"]);
            $('#login').html(USER["login"]);
            $('#inputNome').val(USER["nome"]);
            $('#inputCPF').val(USER["cpf"]);
            $('#inputLogin').val(USER["login"]);

            html = ''
            USER["cupons"].forEach(cupom => {
                html = html+'<div class="card my-2">\n\
                            <div class="card-body">\n\
                                <span>'+cupom["cod"]+'</span> | <span>'+cupom["categoria"]+'</span> | <span>Mínimo: R$ '+parseFloat(cupom["valorMinimo"]).toFixed(2)+'</span> | <span>Desconto: '+parseFloat(cupom["desconto"])*100+'%</span>\n\
                            </div>\n\
                        </div>';
            })
            $("#cupons").html(html+$('#cupons').html())
            $("#addCupom").click(function (e) { 
                Swal.fire({
                    title: 'Digite o código do cupom:',
                    input: 'text',
                    inputAttributes: {
                    autocapitalize: 'off'
                    },
                    showCancelButton: true,
                    cancelButtonText: 'Cancelar',
                    confirmButtonText: 'Validar',
                    showLoaderOnConfirm: true,
                    preConfirm: (cod) => {
                    return eel.validarCupom(cod)()
                        .then(response => {
                        if (response["error"] != null && response["error"] != undefined) {
                            throw new Error(response["error"])
                        }
                        return response
                        })
                        .catch(error => {
                        Swal.showValidationMessage(
                            `${error}`
                        )
                        })
                    },
                    allowOutsideClick: () => !Swal.isLoading()
                }).then((result) => {
                    USER["cupons"].push(result)
                    Swal.fire('Cupom adicionado', '', 'success')
                    location.reload()
                })
            });

            Object.keys(USER["historicoPedidos"]).forEach(key => {
                pedido = USER["historicoPedidos"][key]
                html = '<div class="card my-2">\n\
                            <div class="card-header">\n\
                                Cód: '+pedido["cod"]+'\n\
                            </div>\n\
                            <div class="card-body">\n\
                                <details>\n\
                                    <summary>Ver Mais</summary>\n\
                                    <span class="fontPyFood h4">Restaurante: </span><span class="h5 nomeRestaurante">'+pedido["loja"]["nome"]+'</span><br>\n\
                                    <span class="fontPyFood h4">Data / Hora: </span><span class="h5">'+pedido["datetime"]+'</span><br>\n\
                                    <span class="fontPyFood h4">Endereço de entrega: </span><span class="h5">'+pedido["enderecoEntrega"]["rua"]+', '+pedido["enderecoEntrega"]["bairro"]+', '+pedido["enderecoEntrega"]["num"]+', '+pedido["enderecoEntrega"]["complemento"]+'- '+pedido["enderecoEntrega"]["cidade"]+'</span><br>\n\
                                    <span class="fontPyFood h4">Produtos comprados: </span><br>\n\
                                    <div class="produtos px-4">\n\
                                    ';
                            Object.keys(pedido["produtosComprados"]).forEach(keyProduto => {
                                produto = pedido["produtosComprados"][keyProduto]
                                produtos = '<span class="h5">'+produto["quantidade"].toString().padStart(2, '0')+' '+produto["produto"]["nome"]+' | ';
                                produto["produto"]["adicionais"].forEach(adicional => {
                                    adicionais = adicional["nome"]+", "
                                    produtos = produtos+adicionais
                                });
                                produtos = produtos.slice(0, -2)+' | R$ '+produto["produto"]["totalProduto"]+' / Un.</span><br>';
                                
                                html = html+produtos
                            });
                            html = html+'</div>\n\
                                                    <span class="fontPyFood h4">Subtotal: </span><span class="h5">R$ '+parseFloat(pedido["subtotal"]).toFixed(2)+'</span><br>\n\
                                                    <span class="fontPyFood h4">Taxa de Entrega: </span><span class="h5">R$ '+parseFloat(pedido["taxaEntrega"]).toFixed(2)+'</span><br>\n\
                                                    <span class="fontPyFood h4">Desc. Cupons: </span><span class="h5">R$ '+parseFloat(pedido['subtotal']+pedido["taxaEntrega"]-pedido["total"]).toFixed(2)+'</span><br>\n\
                                                    <span class="fontPyFood h4">Total: </span><span class="h5">R$ '+parseFloat(pedido["total"]).toFixed(2)+'</span><br>\n\
                                                </details>\n\
                                            </div>\n\
                                        </div>'
                $("#pedidos").append(html)
            });
        } else{
            $('#searchVenda').on('input', function() {
                var filtro = $(this).val().toLowerCase();
                
                // Filtrar os cards de pedidos
                $('#vendas .card').hide().filter(function() {
                  var cliente = $(this).find('.cliente').text().toLowerCase();
                  return cliente.includes(filtro);
                }).show();
            });

            console.log(USER["historicoVendas"])
            Object.keys(USER["historicoVendas"]).forEach(key => {
                pedido = USER["historicoVendas"][key]
                html = '<div class="card my-2">\n\
                            <div class="card-header">\n\
                                Cód: '+pedido["cod"]+'\n\
                            </div>\n\
                            <div class="card-body">\n\
                                <details>\n\
                                    <summary>Ver Mais</summary>\n\
                                    <span class="fontPyFood h4">Cliente: </span><span class="h5 cliente">'+pedido["cliente"]["nome"]+'</span><br>\n\
                                    <span class="fontPyFood h4">Data / Hora: </span><span class="h5">'+pedido["datetime"]+'</span><br>\n\
                                    <span class="fontPyFood h4">Endereço de entrega: </span><span class="h5">'+pedido["enderecoEntrega"]["rua"]+', '+pedido["enderecoEntrega"]["bairro"]+', '+pedido["enderecoEntrega"]["num"]+', '+pedido["enderecoEntrega"]["complemento"]+'- '+pedido["enderecoEntrega"]["cidade"]+'</span><br>\n\
                                    <span class="fontPyFood h4">Produtos comprados: </span><br>\n\
                                    <div class="produtos px-4">\n\
                                    ';
                            Object.keys(pedido["produtosComprados"]).forEach(keyProduto => {
                                produto = pedido["produtosComprados"][keyProduto]
                                produtos = '<span class="h5">'+produto["quantidade"].toString().padStart(2, '0')+' '+produto["produto"]["nome"]+' | ';
                                produto["produto"]["adicionais"].forEach(adicional => {
                                    adicionais = adicional["nome"]+", "
                                    produtos = produtos+adicionais
                                });
                                produtos = produtos.slice(0, -2)+' | R$ '+produto["produto"]["totalProduto"]+' / Un.</span><br>';
                                
                                html = html+produtos
                            });
                            html = html+'</div>\n\
                                                    <span class="fontPyFood h4">Subtotal: </span><span class="h5">R$ '+parseFloat(pedido["subtotal"]).toFixed(2)+'</span><br>\n\
                                                    <span class="fontPyFood h4">Taxa de Entrega: </span><span class="h5">R$ '+parseFloat(pedido["taxaEntrega"]).toFixed(2)+'</span><br>\n\
                                                    <span class="fontPyFood h4">Desc. Cupons: </span><span class="h5">R$ '+parseFloat(pedido['subtotal']+pedido["taxaEntrega"]-pedido["total"]).toFixed(2)+'</span><br>\n\
                                                    <span class="fontPyFood h4">Total: </span><span class="h5">R$ '+parseFloat(pedido["total"]).toFixed(2)+'</span><br>\n\
                                                </details>\n\
                                            </div>\n\
                                        </div>'
                $("#vendas").append(html)
            });

            endereco = USER["endereco"]["complemento"] == "" ? USER["endereco"]["rua"]+", "+USER["endereco"]["bairro"]+", "+USER["endereco"]["num"]+", "+USER["endereco"]["complemento"]+", "+USER["endereco"]["cep"]+" - "+USER["endereco"]["cidade"] : USER["endereco"]["rua"]+", "+USER["endereco"]["bairro"]+", "+USER["endereco"]["num"]+", "+USER["endereco"]["cep"]+" - "+USER["endereco"]["cidade"]
            $('h1').html(USER["nome"]+" - Profile");
            $('#nomeLoja').html(USER["nome"]);
            $('#categoriaLoja').html(USER["categoria"]);
            $('#loginLoja').html(USER["login"]);
            $('#enderecoLoja').html(limitarTexto(endereco, 30))
            $('#totalVendas').html("R$"+"<br>"+parseFloat(USER["totalVendas"]).toFixed(2))
            $('#qntVendas').html(USER["quantidadeVendas"]+"<br>"+"Venda(s)")
            $('#inputNome').val(USER["nome"]);
            $('#inputLogin').val(USER["login"]);
            $('#inputCidade').val(USER["endereco"]["cidade"]);
            $('#inputBairro').val(USER["endereco"]["bairro"]);
            $('#inputRua').val(USER["endereco"]["rua"]);
            $('#inputNum').val(USER["endereco"]["num"]);
            $('#inputComplemento').val(USER["endereco"]["complemento"]);
            $('#inputCEP').val(USER["endereco"]["cep"]);
        
            $('#modalEditarDadosLoja').on('shown.bs.modal', function () {
                getAllCategories().then((categorias) => {
                    console.log(categorias)
                    options = ''
                    categorias.forEach(categoria => {
                        options = options + '<option value="'+categoria+'">'+categoria+'</option>'
                    });
                    $("#inputCategoria").append(options)
    
                    $("#inputCategoria").val(USER["categoria"]).trigger("change");
                })
                $("#inputCategoria").select2({
                    tags: true,
                    width: '100%',
                    theme: "classic",
                    dropdownParent: $('#modalEditarDadosLoja')
                });
              });

            $("#editarDadosLoja").submit(function (e) { 
                e.preventDefault();
                endereco = {}
                endereco["cidade"] = $("#inputCidade").val()
                endereco["bairro"] = $("#inputBairro").val()
                endereco["rua"] = $("#inputRua").val()
                endereco["num"] = $("#inputNum").val()
                endereco["complemento"] = $("#inputComplemento").val()
                endereco["cep"] = $("#inputCEP").val()
                var senha = $('#inputSenha').val()
                var nome = $('#inputNome').val()
                var categoria = $('#inputCategoria').val()
                
                Swal.fire({
                    title: "Carregando...",
                    showConfirmButton: false,
                    allowOutsideClick: false,
                    willOpen: () => {
                      Swal.showLoading();
                    }
                });
                editProfileLoja(nome, categoria, endereco, USER["login"], senha).then(() => {
                    Swal.close();
                    Swal.fire('Alterações foram salvas!', '', 'success')
                    $('#modalEditarDadosLoja').modal('hide')
                    location.reload()
                })
            });
        }

        
    }).catch(() => {
        Swal.close();
    });

    
});

async function loadUser(){
    USER = await eel.logar()()
    if(USER["cpf"] != null){
        USER["type"] = "cliente"
    } else{
        USER["type"] = "loja"
    }
}

async function logout(){
    eel.logout()()
}

async function editProfileCliente(nome, cpf, login, senha){
    value = {}
    value["nome"] = nome
    value["cpf"] = cpf
    value["login"] = login
    value["senha"] = senha
    eel.editUser(value)
    USER["nome"] = nome
    USER["cpf"] = cpf
    USER["login"] = login
    USER["senha"] = senha
}

async function editProfileLoja(nome, categoria, endereco, login, senha){
    value = {}
    value["nome"] = nome
    value["categoria"] = categoria
    value["endereco"] = endereco
    value["login"] = login
    value["senha"] = senha
    eel.editUser(value)
    USER["nome"] = nome
    USER["categoria"] = categoria
    USER["endereco"] = endereco
    USER["login"] = login
    USER["senha"] = senha
}

async function deleteUser(){
    return await eel.deleteUser()()
}

async function getAllCategories(){
    return await eel.getAllCategories()()
}

function limitarTexto(texto, limite) {
    if (texto.length > limite) {
      texto = texto.substring(0, limite) + "...";
    }
    return texto;
}