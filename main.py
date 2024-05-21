from flask import Flask, url_for, render_template


#Inicialização
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuarios"

    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "João", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": False}
    ]

    return render_template('index.html', titulo=titulo, usuarios=usuarios)


@app.route('/sobre')
def pagina_sobre():
    return """
        <b>Programador Python </b>
        """

app.run(debug=True)