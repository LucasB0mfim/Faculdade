# Importa a instância da aplicação Flask (app) do módulo app
from app import app

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento Flask com o modo de depuração ativado
    app.run(debug=True)