# Importa os objetos request e render_template do módulo flask e a instância da aplicação Flask (app) do módulo app
from flask import request, render_template
from app import app

# Define uma rota dinâminca padrão
@app.route('/')
def index():
    boasVindas = '<h1>Olá!</h1>'
    direcionar = '<p>Coloque seu nome depois da porta para receber uma saudação! Exemplo: http://127.0.0.1:5000/Lucas</p>'
    return boasVindas + direcionar


# Define uma rota que recebe um parâmetro nome
@app.route('/<nome>')
def colocaNome(nome): 
    # Retorna um template HTML chamado index.html, passando o parâmetro nome_recebido para ser renderizado no template
    return render_template('index.html', nome_recebido=nome)

# Define uma função que retorna uma saudação personalizada
def ola(nome):
    return "Olá, ", {"nome_recebido": nome} 

# Define a rota /logar que pode ser acessada por métodos GET e POST
@app.route('/logar', methods=['GET', 'POST'])
def logar():
    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Retorna uma mensagem indicando que a requisição POST foi recebida
        return "Recebeu post! Fazer login!"
    else:
        # Retorna uma mensagem indicando que a requisição GET foi recebida
        return "Recebeu get! Fazer login!"