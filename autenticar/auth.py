# Função para carregar usuários e senhas do arquivo JSON

import json
import bcrypt

def load_users():
    with open("autenticacao/usuarios.json", "r") as file:
        users = json.load(file)["users"]
    return users

# Função para verificar credenciais
def verify_credentials(username, password):
    users = load_users()
    for user in users:
        stored_password = user["password"].encode('utf-8')
        if user["username"] == username and bcrypt.checkpw(password.encode('utf-8'), stored_password):
            return True
    return False