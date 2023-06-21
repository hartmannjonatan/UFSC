let USER = null

$(document).ready(function() {

    $('form').submit(function(event) {
        event.preventDefault(); // Evita o envio padrão do formulário

        var login = $('#login').val();
        var senha = $('#senha').val()
        var type = $('input[name="type"]:checked').val()
        
        logar(login, senha, type);
    });
});

async function logar(login, senha, type){
    let dados = await eel.logar(type, login, senha)()
    console.log(dados)
    if("error" in dados){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: dados.error
          })
    } else{
        window.location.href = "./index.html"
    }
}