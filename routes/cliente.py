from flask import Blueprint
cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """Listar os Clientes"""
    pass

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente """
    pass
    
@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar um cliente """
    pass    

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalhes do cliente """
    pass  

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente (cliente_id):
    """ Formulario para editar um cliente """
    pass  

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente (cliente_id):
    """ Atualizar informações do cliente """
    pass  

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente (cliente_id):
    """ Deletar um cliente """
    pass  