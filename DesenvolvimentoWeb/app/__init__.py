# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância da aplicação Flask com o nome do módulo atual (__name__)
app = Flask(__name__)

# Configura o modo de depuração da aplicação para True
app.debug = True

# Importa o módulo routes, que contém as rotas e a lógica do aplicativo
from app import routes