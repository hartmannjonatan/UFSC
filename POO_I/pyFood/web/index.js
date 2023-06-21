let USER = null
let LOJASDATA = {}

$(document).ready(function() {
    
    $(".logout").click(function (e) { 
        logout().then(() =>  {
            window.location.href = "./login.html"
        })
    });

    Swal.fire({
        title: "Carregando dados...",
        showConfirmButton: false,
        allowOutsideClick: false,
        willOpen: () => {
          Swal.showLoading();
        }
    });
    loadUser().then(() => {
        console.log(USER)
        Swal.close();
        if(USER == null || USER == undefined || USER["error"] != undefined){
            window.location.href = "./login.html"
        }
        $("#not"+USER["type"]).remove();
        if(USER["type"] == "cliente"){
            getAllLojas().then((lojas) => {
                cuponsCategorias = []
                USER["cupons"].forEach(cupom => {
                    cuponsCategorias.push(cupom["categoria"])
                })
                categorias = []
                Object.keys(lojas).forEach(key  => {
                    loja = lojas[key]
                    LOJASDATA[loja["login"]] = loja
                    categorias.push(loja["categoria"])
                    cupomDisponivel = ""
                    if(cuponsCategorias.includes(loja["categoria"]) || cuponsCategorias.includes("QUALQUER_CATEGORIA")){
                        cupomDisponivel = "Cupom disponível!"
                    }
                    html ='<div data-lojaid="'+loja["login"]+'" data-categoria="'+loja["categoria"]+'" class="pedidoLoja">\n\
                                <div class="card my-2 cardLoja">\n\
                                    <div class="card-body d-flex justify-content-between px-5">\n\
                                        <div class="h5 nomeRestaurante">'+loja["nome"]+'</div>\n\
                                        <div class="h5 text-success">'+cupomDisponivel+'</div>\n\
                                    </div>\n\
                                </div>\n\
                            </div>'
                    $('#escolherLojas').append(html)
                })
                $(".pedidoLoja").click(function (e) { 
                    openPedidoLoja($(this).data('lojaid'))
                });
                htmlCategorias = '<option selected disabled value="todas">Escolha uma categoria</option>\n\
                                    <option value="QUALQUER_CATEGORIA">Todas</option>'
                categorias.forEach(categoria => {
                    htmlCategorias = htmlCategorias+'<option value="'+categoria+'">'+categoria+'</option>'
                })
                $('#searchCategoria').html(htmlCategorias)
            })

            $('#searchLoja').on('input', function() {
                var filtro = $(this).val().toLowerCase();
                
                // Filtrar os cards de pedidos
                $('#escolherLojas .card').hide().filter(function() {
                  var restaurante = $(this).find('.nomeRestaurante').text().toLowerCase();
                  return restaurante.includes(filtro);
                }).show();
            });

            $('#searchCategoria').on('change', function() {
                var filtro = $(this).val().toLowerCase();
                
                // Filtrar os cards de pedidos
                $('#escolherLojas .pedidoLoja').hide().filter(function() {
                    var categoria = $(this).data('categoria').toLowerCase();
                    return (filtro === "qualquer_categoria" || categoria === filtro);
                }).show();
              });
        } else{
            console.log(USER["produtos"])
            USER["produtos"].forEach(produto => {
                console.log(produto)
                htmlAdicionais = ''
                produto["adicionais"].forEach(adicional => {
                    htmlAdicionais = htmlAdicionais + '<div id="cardAdicional'+adicional["cod"]+'Produto'+produto["cod"]+'" data-adicionalcod="'+adicional["cod"]+'" class="card my-2 cardAdicional">\n\
                                                            <div class="card-body d-flex justify-content-between px-5">\n\
                                                                <div class="h5">'+adicional["nome"]+' <span class="h5 text-success">+ R$ '+parseFloat(adicional["valorAdicional"]).toFixed(2)+'</span></div>\n\
                                                                <div>\n\
                                                                    <button data-codadicional="'+adicional["cod"]+'" data-codproduto="'+produto["cod"]+'" class="btn btn-primary mx-2 editarAdicional">Editar</button>\n\
                                                                    <button data-codadicional="'+adicional["cod"]+'" data-codproduto="'+produto["cod"]+'" class="btn btn-danger mx-2 deletarAdicional">Deletar</button>\n\
                                                                </div>\n\
                                                            </div>\n\
                                                        </div>\n\
                                                        <form id="editAdicional'+adicional["cod"]+'Produto'+produto["cod"]+'" class="d-none editAdicionalForm" data-codadicional="'+adicional["cod"]+'" data-codproduto="'+produto["cod"]+'">\n\
                                                            <div class="d-flex justify-content-between my-2">\n\
                                                                <input required type="text" class="form-control mx-2" id="inputEditNomeAdicional'+adicional["cod"]+'Produto'+produto["cod"]+'" placeholder="Digite o nome do adicional" value="'+adicional["nome"]+'">\n\
                                                                <input required type="text" class="form-control mx-2 inputValorAdicional" id="inputEditValorAdicional'+adicional["cod"]+'Produto'+produto["cod"]+'" placeholder="Valor do adicional" value="'+adicional["valorAdicional"]+'"></input>\n\
                                                                <div class="invalid-feedback">\n\
                                                                    Por favor, insira um valor válido.\n\
                                                                </div>\n\
                                                                <button type="submit" class="btn btn-success mx-2">Salvar</button>\n\
                                                            </div>\n\
                                                        </form>'
                })
    
                html = '<button type="button" style="all: unset;" data-toggle="modal" data-target="#modal'+produto["cod"]+'" class="w-100">\n\
                            <div class="card my-2 cardProduto">\n\
                                <div class="card-body d-flex justify-content-between px-5">\n\
                                    <div class="h5 nomeProduto">'+produto["nome"]+'</div>\n\
                                    <div class="h6">'+limitarTexto(produto["descricao"], 80)+'</div>\n\
                                    <div class="h5 text-success">R$ '+parseFloat(produto["valor"]).toFixed(2)+'</div>\n\
                                </div>\n\
                            </div>\n\
                        </button>\n\
                        <div class="modal modal-lg fade" id="modal'+produto["cod"]+'" data-produtocod="'+produto["cod"]+'" tabindex="-1" role="dialog" aria-hidden="true">\n\
                            <div class="modal-dialog" role="document">\n\
                                <div class="modal-content">\n\
                                    <div class="modal-header">\n\
                                        <div class="d-flex justify-content-between w-100">\n\
                                            <div>\n\
                                                <h4 class="modal-title fontPyFood" id="exampleModalLabel">'+produto["nome"]+'</h4>\n\
                                            </div>\n\
                                            <div>\n\
                                                <button class="btn btn-primary mx-2 btnEditarProduto" data-codproduto="'+produto["cod"]+'" id="editarProduto'+produto["cod"]+'">Editar Produto</button>\n\
                                                <button class="btn btn-danger mx-2 btnDeletarProduto" data-codproduto="'+produto["cod"]+'">Deletar Produto</button>\n\
                                            </div>\n\
                                        </div>\n\
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">\n\
                                        <span aria-hidden="true">&times;</span>\n\
                                        </button>\n\
                                    </div>\n\
                                    <div class="modal-body">\n\
                                        <span class="fontPyFood h5">Descrição: </span><span>'+produto["descricao"]+'</span><br>\n\
                                        <span class="fontPyFood h5">Valor: </span><span>R$ '+parseFloat(produto["valor"]).toFixed(2)+'</span><br>\n\
                                        <hr>\n\
                                        <div class="d-flex justify-content-between">\n\
                                            <div class="fontPyFood h5">Adicionais:</div>\n\
                                            <div><button data-codproduto="'+produto["cod"]+'" class="btn btn-success mx-2 btnAddAdicional">+ Adicional</button></div>\n\
                                        </div>\n\
                                        <form id="novoAdicional'+produto["cod"]+'" class="d-none novoAdicionalForm" data-codproduto="'+produto["cod"]+'">\n\
                                            <div id="addAdicional'+produto["cod"]+'" class="d-flex justify-content-between my-2">\n\
                                                <input required type="text" class="form-control mx-2" id="inputNomeAdicional'+produto["cod"]+'" placeholder="Digite o nome do adicional">\n\
                                                <input required type="text" class="form-control mx-2 inputValorAdicional" id="inputValorAdicional'+produto["cod"]+'" placeholder="Valor do adicional"></input>\n\
                                                <div class="invalid-feedback">\n\
                                                    Por favor, insira um valor válido.\n\
                                                </div>\n\
                                                <button type="submit" class="btn btn-success mx-2">Salvar</button>\n\
                                            </div>\n\
                                        </form>\n\
                                        <div id="adicionais">\n\
                                            '+htmlAdicionais+'\n\
                                        </div>\n\
                                    </div>\n\
                                </div>\n\
                            </div>\n\
                        </div>'
                $('#meusProdutos').append(html)

                $(".btnDeletarProduto").click(function (e) { 
                    e.preventDefault();
                    codProduto = parseInt($(this).attr("data-codproduto"))
                    Swal.fire({
                        title: 'Você realmente deseja deletar este produto?',
                        icon: 'warning',
                        showCancelButton: true,
                        confirmButtonText: 'Sim',
                        cancelButtonText: 'Cancelar'
                      }).then((result) => {
                        if (result.isConfirmed) {
                            deleteProduto(codProduto).then((data) => {
                                if(data["delete"] == "success"){
                                    let timerInterval
                                    Swal.fire({
                                        title: 'Produto deletado!',
                                        timer: 2000,
                                        timerProgressBar: true,
                                        willClose: () => {
                                            clearInterval(timerInterval)
                                        }
                                    }).then((result) => {
                                        window.location.reload()
                                    })
                                }
                            })
                        }
                    });
                });

                $(".editAdicionalForm").submit(function (e) { 
                    e.preventDefault();
                    codProduto = parseInt($(this).attr("data-codproduto"))
                    codAdicional = parseInt($(this).attr("data-codadicional"))
                    adicional = {}
                    adicional["nome"] = $("#inputEditNomeAdicional"+codAdicional+"Produto"+codProduto).val()
                    adicional["valorAdicional"] = parseFloat($("#inputEditValorAdicional"+codAdicional+"Produto"+codProduto).val())
                    adicional["cod"] = codAdicional
                    editAdicional(codProduto, adicional).then((data) => {
                        let timerInterval
                        Swal.fire({
                            title: 'Adicional alterado',
                            timer: 2000,
                            timerProgressBar: true,
                            willClose: () => {
                                clearInterval(timerInterval)
                            }
                        }).then((result) => {
                            location.reload()
                        })
                    })
                    
                });

                $(".editarAdicional").click(function (e) { 
                    codProduto = parseInt($(this).attr("data-codproduto"))
                    codAdicional = parseInt($(this).attr("data-codadicional"))
                    $("#editAdicional"+codAdicional+"Produto"+codProduto).removeClass("d-none")
                    $("#cardAdicional"+codAdicional+"Produto"+codProduto).addClass("d-none")
                });

                $(".btnAddAdicional").click(function (e) { 
                    $("#novoAdicional"+$(this).attr("data-codproduto")).removeClass("d-none")
                });

                $(".deletarAdicional").click(function (e) { 
                    e.preventDefault();
                    codProduto = parseInt($(this).attr("data-codproduto"))
                    codAdicional = parseInt($(this).attr("data-codadicional"))
                    Swal.fire({
                        title: 'Você realmente deseja deletar este adicional?',
                        icon: 'warning',
                        showCancelButton: true,
                        confirmButtonText: 'Sim',
                        cancelButtonText: 'Cancelar'
                      }).then((result) => {
                        if (result.isConfirmed) {
                            deleteAdicional(codProduto, codAdicional).then((data) => {
                                if(data["delete"] == "success"){
                                    let timerInterval
                                    Swal.fire({
                                        title: 'Adicional deletado!',
                                        timer: 2000,
                                        timerProgressBar: true,
                                        willClose: () => {
                                            clearInterval(timerInterval)
                                        }
                                    }).then((result) => {
                                        window.location.reload()
                                    })
                                }
                            })
                        }
                    });
                });

                $(".btnEditarProduto").click(function (e) { 
                    cod = parseInt($(this).attr("data-codproduto"))
                    produto = USER["produtos"][cod]
                    $("#formDadosProduto").attr("data-editar", "true")
                    $("#formDadosProduto").attr("data-codproduto", cod)
                    $("#modalNovoProduto").attr("data-editar", "true")
                    $("#modalNovoProduto").attr("data-codproduto", cod)
                    $("#inputNomeProduto").val(produto["nome"])
                    $("#inputDescricao").val(produto["descricao"])
                    $("#inputValor").val(produto["valor"])
                    $("#modalNovoProduto").modal('show')
                });

                // Validar o campo de valor monetário
                $(".inputValorAdicional").on("input", function() {
                    var valor = $(this).val();
                    var regex = /(^R\$ )?(\d+(\.)?)+(\,\d{1,2})?$/gm;
                    var valido = regex.test(valor);
                
                    if (valido) {
                    $(this).removeClass("is-invalid");
                    $(this).addClass("is-valid");
                    } else {
                    $(this).removeClass("is-valid");
                    $(this).addClass("is-invalid");
                    }
                });

                $(".novoAdicionalForm").submit(function (e) { 
                    e.preventDefault();
                    adicional = {}
                    adicional["nome"] = $("#inputNomeAdicional"+$(this).attr("data-codproduto")).val()
                    adicional["valor"] = parseFloat($("#inputValorAdicional"+$(this).attr("data-codproduto")).val())
                    addAdicional(parseInt($(this).attr("data-codproduto")), adicional).then((data) => {
                        if(data["newAdicional"] == "success"){
                            let timerInterval
                            Swal.fire({
                                title: 'Adicional cadastrado!',
                                timer: 2000,
                                timerProgressBar: true,
                                willClose: () => {
                                    clearInterval(timerInterval)
                                }
                            }).then((result) => {
                                location.reload()
                            })
                        }
                    })
                });
            });

            $('#searchProduto').on('input', function() {
                var filtro = $(this).val().toLowerCase();
                
                // Filtrar os cards de pedidos
                $('#meusProdutos .card').hide().filter(function() {
                  var produto = $(this).find('.nomeProduto').text().toLowerCase();
                  return produto.includes(filtro);
                }).show();
            });

            // Validar o campo de valor monetário
            $("#inputValor").on("input", function() {
                var valor = $(this).val();
                var regex = /(^R\$ )?(\d+(\.)?)+(\,\d{1,2})?$/gm;
                var valido = regex.test(valor);
              
                if (valido) {
                  $(this).removeClass("is-invalid");
                  $(this).addClass("is-valid");
                } else {
                  $(this).removeClass("is-valid");
                  $(this).addClass("is-invalid");
                }
            });
            
            $("#submitFormEnvioProduto").click(function (e) { 
                e.preventDefault();
                $('#formDadosProduto').submit()
            });

            $("#formDadosProduto").submit(function (e) { 
                e.preventDefault();
                
                if($(this).attr("data-editar") == "false"){
                    produto = {}
                    produto["nome"] = $("#inputNomeProduto").val()
                    produto["descricao"] = $("#inputDescricao").val()
                    produto["valor"] = parseFloat($("#inputValor").val())
                    newProduto(produto).then((data) => {
                        let timerInterval
                        Swal.fire({
                            title: 'Produto cadastrado!',
                            timer: 2000,
                            timerProgressBar: true,
                            willClose: () => {
                                clearInterval(timerInterval)
                            }
                        }).then((result) => {
                            location.reload()
                        })
                    }).catch((error) => {
                        console.log(error)
                    })
                } else{
                    cod = parseInt($(this).attr("data-codproduto"))
                    produto = USER["produtos"][cod]
                    produto["nome"] = $("#inputNomeProduto").val()
                    produto["descricao"] = $("#inputDescricao").val()
                    produto["valor"] = parseFloat($("#inputValor").val())
                    editProduto(produto).then((data) => {
                        let timerInterval
                        Swal.fire({
                            title: 'Produto alterado!',
                            timer: 2000,
                            timerProgressBar: true,
                            willClose: () => {
                                clearInterval(timerInterval)
                            }
                        }).then((result) => {
                            location.reload()
                        })
                    }).catch((error) => {
                        console.log(error)
                    })
                }
            });
        }

    }).catch(() => {
        Swal.close();
    });

    
});

function openPedidoLoja (lojaId){
    localStorage.setItem('dados', JSON.stringify(LOJASDATA[lojaId]));
    window.location.href = 'pedido.html';
}

function limitarTexto(texto, limite) {
    if (texto.length > limite) {
      texto = texto.substring(0, limite) + "...";
    }
    return texto;
}

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

async function getAllLojas(){
    return await eel.getAllLojas()()
}

async function newProduto(produto){
    return await eel.newProduto(produto)()
}

async function editProduto(produto){
    return await eel.editProduto(produto)()
}

async function addAdicional(codProduto, adicional){
    return await eel.addAdicional(codProduto, adicional)()
}

async function editAdicional(codProduto, adicional){
    return await eel.editAdicional(codProduto, adicional)
}

async function deleteAdicional(codProduto, codAdicional){
    return await eel.deleteAdicional(codProduto,codAdicional)()
}

async function deleteProduto(codProduto){
    return await eel.deleteProduto(codProduto)()
}