from flask import Blueprint, render_template, request
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """Listar os Clientes"""
    return render_template('lista_clientes.html',clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente """

    data = request.json

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }

    CLIENTES.append(novo_usuario)


    return render_template('item_cliente.html', cliente=novo_usuario)
    
    
@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar um cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalhes do cliente """
    return render_template('detalhe_cliente.html')  

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente (cliente_id):
    """ Formulario para editar um cliente """
    return render_template('form_edit_cliente.html')  

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente (cliente_id):
    """ Atualizar informações do cliente """
    pass  

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    """ Deletar um cliente """
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]  
    return {'deleted': 'ok'}