import bcrypt
import sqlite3
'''
### METODO DE ENCODING
O UTF-8 é o padrão dominante de codificação de caracteres na web, 
mapeando caracteres Unicode para sequências de 1 a 4 bytes, 
garantindo compatibilidade com ASCII.
'''
# DB =======================================================================================
connection = sqlite3.connect("banco.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE login_info (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               login TEXT NOT NULL,
               senha TEXT NOT NULL
               )""")
connection.commit()
# FUNÇOES ==================================================================================
def bcrypt_hash(password:str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))

    return hashed_password

def verify_password(password:str, hashed_pass:bytes):
    return bcrypt.checkpw(password.encode('utf-8'),hashed_pass)

def login_pass(username:str, password:str):
    login_cadastrado = "admin"
    senha_cadastrada = "admin123@"

    if username == login_cadastrado and password == senha_cadastrada:
        if verify_password(user_pass, hashed):
            print("Senha verifica com sucesso!")
        else:
            print("Falha na verificação")
        print("Login efetuado com sucesso!")

# ==========================================================================================
'''
print("===== RANDOM WEBSITE LOGIN =====")

login = str(input("Login: "))

user_pass = str(input("Senha: "))

hashed = bcrypt_hash(user_pass)

'''



