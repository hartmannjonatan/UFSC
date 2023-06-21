let USER = null
let loja = null
let PEDIDO = {}

$(document).ready(function() {
    PEDIDO["produtosComprados"] = []
    loja = JSON.parse(localStorage.getItem("dados"))

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
        console.log(loja)
        Swal.close();
        if(USER == null || USER == undefined || USER["error"] != undefined){
            window.location.href = "./login.html"
        }
        
        $("h1").html(loja["nome"]+" | Faça seu pedido!");
        endereco = ''
        if(loja["endereco"]["complemento"] == null){
            endereco = '<span class="fontPyFood h5">Endereço: </span><span>'+loja["endereco"]["rua"]+', '+loja["endereco"]["num"]+', '+loja["endereco"]["bairro"]+' - '+loja["endereco"]["cidade"]+'</span><br>'
        } else{
            endereco= '<span class="fontPyFood h5">Endereço: </span><span>'+loja["endereco"]["rua"]+', '+loja["endereco"]["num"]+', '+loja["endereco"]["complemento"]+', '+loja["endereco"]["bairro"]+' - '+loja["endereco"]["cidade"]+'</span><br>'
        }
        htmlDadosLoja = '<summary>Dados da loja</summary>\n\
                        <span class="fontPyFood h5">Cód.: </span><span>'+loja["login"]+'</span><br>\n\
                        <span class="fontPyFood h5">Categoria: </span><span>'+loja["categoria"]+'</span><br>\n\
                        '+endereco+'\n\
                        <span class="fontPyFood h5">Vendas realizadas: </span><span>'+loja["quantidadeVendas"]+'</span><br>'
        $("#dadosLoja").html(htmlDadosLoja)

        for (var key in USER["cupons"]) {
            var cupom = USER["cupons"][key];
            $("#selectCupom").append('<option value="'+key+'">'+cupom["cod"]+'</option>')
        }

        loja["produtos"].forEach(produto => {
            htmlAdicionais = ''
            produto["adicionais"].forEach(adicional => {
                htmlAdicionais = htmlAdicionais + '<div data-selected="false" data-adicionalcod="'+adicional["cod"]+'" class="card my-2 cardAdicional">\n\
                                                        <div class="card-body d-flex justify-content-between px-5">\n\
                                                            <div class="h5">'+adicional["nome"]+' <span class="h5 text-success">+ R$ '+parseFloat(adicional["valorAdicional"]).toFixed(2)+'</span></div>\n\
                                                            <div><input style="cursor: pointer;" type="checkbox" class="form-check-input selectAdicional" id="adicional'+adicional["cod"]+'"></div>\n\
                                                        </div>\n\
                                                    </div>'
            })

            html = '<button type="button" style="all: unset;" data-toggle="modal" data-target="#modal'+produto["cod"]+'" class="w-100">\n\
                        <div class="card my-2 cardProduto">\n\
                            <div class="card-body d-flex justify-content-between px-5">\n\
                                <div class="h5">'+produto["nome"]+'</div>\n\
                                <div class="h6">'+limitarTexto(produto["descricao"], 80)+'</div>\n\
                                <div class="h5 text-success">R$ '+parseFloat(produto["valor"]).toFixed(2)+'</div>\n\
                            </div>\n\
                        </div>\n\
                    </button>\n\
                    <div class="modal modal-lg fade" id="modal'+produto["cod"]+'" data-produtocod="'+produto["cod"]+'" tabindex="-1" role="dialog" aria-hidden="true">\n\
                        <div class="modal-dialog" role="document">\n\
                            <div class="modal-content">\n\
                                <div class="modal-header">\n\
                                    <h4 class="modal-title fontPyFood" id="exampleModalLabel">'+produto["nome"]+'</h4>\n\
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">\n\
                                    <span aria-hidden="true">&times;</span>\n\
                                    </button>\n\
                                </div>\n\
                                <div class="modal-body">\n\
                                    <span class="fontPyFood h5">Descrição: </span><span>'+produto["descricao"]+'</span><br>\n\
                                    <hr>\n\
                                    <div id="adicionais">\n\
                                        '+htmlAdicionais+'\n\
                                    </div>\n\
                                </div>\n\
                                <div class="modal-footer d-flex justify-content-between px-4">\n\
                                        <div class="form-group mb-2">\n\
                                            <label for="inputQuantidade'+produto["cod"]+'">Quantidade:</label>\n\
                                            <input min="1" type="number" class="form-control-number" id="inputQuantidade'+produto["cod"]+'" value="1">\n\
                                        </div>\n\
                                        <button type="submit" class="btn btn-primary mb-2 adicionarProduto">Adicionar ao pedido</button>\n\
                                </div>\n\
                            </div>\n\
                        </div>\n\
                    </div>'
            $('#escolherProdutos').append(html)
        });

        $('.selectAdicional').on('change', function() {
            if($(this).closest('.cardAdicional').attr("data-selected") == "on"){
                $(this).closest('.cardAdicional').attr('data-selected', "false");
            } else{
                $(this).closest('.cardAdicional').attr('data-selected', $(this).val());
            }
        });

        $(".adicionarProduto").click(function (e) { 
            modal = $(this).closest('.modal')
            produto = loja["produtos"][modal.data("produtocod")]
            quantidade = $("#inputQuantidade"+produto["cod"]).val()
            var listaAdicionais = [];
            $('#'+modal.attr("id")+' .cardAdicional').each(function() {
                if($(this).attr("data-selected") == "on"){
                    var id = $(this).data("adicionalcod");
                    listaAdicionais.push(id);
                }
            });

            aux = {}
            aux["quantidade"] = quantidade
            aux["produto"] = produto
            adicionais = []
            listaAdicionais.forEach(adicional => {
                adicionais.push(produto["adicionais"][adicional])
            })
            aux["adicionais"] = adicionais
            PEDIDO["produtosComprados"].push(aux)
            atualizarPedido()
            $('#'+modal.attr("id")).modal('hide')


        });

        $("#cancelarPedido").click(function (e) { 
            PEDIDO = {}
            PEDIDO["produtosComprados"] = []
            atualizarPedido()
            location.reload()
        });

        $("#emitirPedido").click(function (e) { 
            if(verificarCamposPreenchidos("inputEndereco")){
                endereco = {}
                endereco["cidade"] = $("#inputCidade").val()
                endereco["bairro"] = $("#inputBairro").val()
                endereco["rua"] = $("#inputRua").val()
                endereco["num"] = $("#inputNum").val()
                endereco["complemento"] = $("#inputComplemento").val()
                endereco["cep"] = $("#inputCEP").val()
                PEDIDO["enderecoEntrega"] = endereco
                cupom = $("#selectCupom").val()
                PEDIDO["cupom"] = cupom
                PEDIDO["taxaEntrega"] = 10.0 // FIXA COMO 10R$
                PEDIDO["loja"] = loja
                PEDIDO["cliente"] = USER

                calcularTotalPedido().then((total) => {
                    taxa = parseFloat(PEDIDO["taxaEntrega"])
                    descCupom = (taxa+parseFloat(PEDIDO["subtotal"]))-total
                    $("#valueTotal").html('R$ '+parseFloat(total).toFixed(2))
                    $("#valueTaxaEntrega").html('R$ '+parseFloat(PEDIDO["taxaEntrega"]).toFixed(2))
                    $("#valueDescontoCupom").html('R$ '+parseFloat(descCupom).toFixed(2))

                    Swal.fire({
                        title: 'Emitir pedido?',
                        showDenyButton: true,
                        confirmButtonText: 'Sim',
                        denyButtonText: `Cancelar`,
                    }).then((result) => {
                        /* Read more about isConfirmed, isDenied below */
                        if (result.isConfirmed) {
                            emitirPedido().then(()=>{
                                let timerInterval
                                Swal.fire({
                                    title: 'Pedido confirmado!',
                                    timer: 2000,
                                    timerProgressBar: true,
                                    willClose: () => {
                                        clearInterval(timerInterval)
                                    }
                                }).then((result) => {
                                    window.location.href = "profile.html"
                                })
                            })
                        }
                    })
                }).catch((error) => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: error
                    })
                })
                
            } else{
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: "O endereço deve ser preenchido corretamente!"
                })

                $("#inputCidade").focus()
            }
        });


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

function limitarTexto(texto, limite) { // PARA A DESCRIÇÃO DO PRODUTO NÃO PASSAR DO MÁXIMO DO CARD
    if (texto.length > limite) {
      texto = texto.substring(0, limite) + "...";
    }
    return texto;
}

function atualizarPedido(){
    if(verificarCamposPreenchidos("inputEndereco")){
        endereco = {}
        endereco["cidade"] = $("#inputCidade").val()
        endereco["bairro"] = $("#inputBairro").val()
        endereco["rua"] = $("#inputRua").val()
        endereco["num"] = $("#inputNum").val()
        endereco["complemento"] = $("#inputComplemento").val()
        endereco["cep"] = $("#inputCEP").val()
        PEDIDO["enderecoEntrega"] = endereco
        cupom = $("#selectCupom").val()
        PEDIDO["cupom"] = cupom
        PEDIDO["taxaEntrega"] = 10.0 // FIXA COMO 10R$
        PEDIDO["loja"] = loja
        PEDIDO["cliente"] = USER
        calcularTotalPedido().then((total) => {
            taxa = parseFloat(PEDIDO["taxaEntrega"])
            descCupom = (taxa+parseFloat(PEDIDO["subtotal"]))-total
            $("#valueTotal").html('R$ '+parseFloat(total).toFixed(2))
            $("#valueTaxaEntrega").html('R$ '+parseFloat(PEDIDO["taxaEntrega"]).toFixed(2))
            $("#valueDescontoCupom").html('R$ '+parseFloat(descCupom).toFixed(2))
        }).catch((error) => {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: error
            })
        })
    } else{
        $("#valueTotal").html('R$ -')
        $("#valueTaxaEntrega").html('R$ -')
        $("#valueDescontoCupom").html('R$ -')
    }

    console.log(PEDIDO["produtosComprados"])
    subtotal = 0
    if(PEDIDO["produtosComprados"].length > 0){
        html = ''
        $("#itemsSacola").html(0)
        PEDIDO["produtosComprados"].forEach((produtoPedido, key) => {
            quantidade = parseInt(produtoPedido["quantidade"])
            $("#itemsSacola").removeClass("d-none");
            $("#itemsSacola").html(parseInt($("#itemsSacola").html())+parseInt(quantidade))
            valor = parseFloat(PEDIDO["produtosComprados"][key]["produto"]["valor"])*quantidade
            produto = produtoPedido["produto"]
            htmlAdicionais = ''
            if(produtoPedido["adicionais"].length > 0){
                htmlAdicionais = '<span class="h5">Adicionais: </span><br>'
                produtoPedido["adicionais"].forEach(adicional => {
                    valor += parseFloat(adicional["valorAdicional"])*quantidade
                    htmlAdicionais = htmlAdicionais+'<span>'+adicional["nome"]+' (R$ '+parseFloat(adicional["valorAdicional"]).toFixed(2)+')</span><br>'
                });
            }
            subtotal += valor
            html = html+'<div class="card my-2 cardProdutoPedido">\n\
                        <div class="card-body px-5">\n\
                            <div class="d-flex justify-content-between">\n\
                                <div class="h5 font-weight-bold">'+quantidade+'</div>\n\
                                <div class="h5">'+produto["nome"]+'</div>\n\
                                <div class="h5 text-success">R$ '+parseFloat(valor).toFixed(2)+'</div>\n\
                                <button data-indexproduto="'+key+'" type="button"class="btn btn-danger btnRemoverProduto">Remover</button>\n\
                            </div>\n\
                            <hr>\n\
                            '+htmlAdicionais+'\n\
                        </div>\n\
                    </div>'
        });
        
        $("#produtosPedidos").html(html)
        $(".btnRemoverProduto").click(function (e) { 
            console.log($(this).attr("data-indexproduto"))
            
            PEDIDO["produtosComprados"].splice($(this).attr("data-indexproduto"), 1)
            atualizarPedido()
        });
    } else{
        $("#produtosPedidos").html("Você ainda não escolheu produtos.")
        $("#itemsSacola").addClass("d-none");
    }
    PEDIDO["subtotal"] = subtotal
    $("#valueSubtotal").html('R$ '+parseFloat(subtotal).toFixed(2))
}

function verificarCamposPreenchidos(divId) {
    var camposPreenchidos = true;
    
    $('#' + divId).find('input[required], select[required], textarea[required]').each(function() {
      if ($(this).val() === '') {
        camposPreenchidos = false;
        return false; // Para interromper o loop caso haja um campo vazio
      }
    });
    
    return camposPreenchidos;
}

async function calcularTotalPedido() {
    console.log(PEDIDO)
    data = await eel.novoPedido(PEDIDO, 1)()
    console.log(data)
    if(data["error"] != undefined && data["error"] != null){
        throw new Error(data["error"])
    } else{
        return data["total"]
    }
}

async function emitirPedido(){
    return await eel.novoPedido(PEDIDO, 0)()
}