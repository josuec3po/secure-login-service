import bcrypt
import sqlite3
'''
### METODO DE ENCODING
O UTF-8 é o padrão dominante de codificação de caracteres na web, 
mapeando caracteres Unicode para sequências de 1 a 4 bytes, 
garantindo compatibilidade com ASCII.
'''
# CRIA DB SE NÃO EXISTIR =======================================================================================
connection = sqlite3.connect("banco.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS login_info (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               login TEXT NOT NULL,
               senha TEXT NOT NULL
               )""")
connection.commit()

# FUNÇOES ==================================================================================

# CRITOGRAFAR A SENHA ======================================================================
def bcrypt_hash(password:str):
    # Encripta a senha
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))
    return hashed_password

# VERIFICAR PASSWORD PARA LOGIN ===========================================================
def verify_password(password:str, hashed_pass:bytes):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_pass)

# FUNCAO PRECISA DE ALTERACOES ============================================================
def login_pass():
    print("LOGIN ====")
    username = str(input("Usuario: "))
    # CONDICAO DE EXISTENCIA USERNAME
    cursor.execute("SELECT login from login_info WHERE login = ?", (username,))
    resultado1 = cursor.fetchone() # COLETA INFORMAÇÃO DO BANCO
    if resultado1 is None:
        print("Usuário não encontrado")
        return
    else:
        pass

    password = str(input("Senha: "))
    # VERIFICAO DE SENHA HASH
    cursor.execute("SELECT senha FROM login_info WHERE login = ?", (username,))
    resultado2 = cursor.fetchone() # Pega a primeira linha encontrada

    hash_do_banco = resultado2[0]
    if bcrypt.checkpw(password.encode('utf-8'), hash_do_banco):
        print("Login efetuado com sucesso!")
    else:
        print("Senha incorreta!")


# REGISTRAR USUARIO ========================================================================
def register_user():
    print("==== CADASTRO DE USUARIO ====")
    username = str(input(("Usuario: ")))
    password = str(input("Senha: "))

    # Senha em hash (OBS:NUNCA SE GUARDA A SENHA ORIGINAL)
    hashed = bcrypt_hash(password)

    # SALVA NO BANCO
    cursor.execute("""INSERT INTO login_info
                    (login, senha) VALUES
                    (?, ?) """, (username, hashed))

# ==========================================================================================

print("="*30, " WEBSITE ", "="*30)
'''
print("[1] Login\n[2] Registrar-se\n[3] Sair")

user_option = int(input("Digite a opção desejada: "))

match user_option:
    case 1:
        
    case 2:
'''


login_pass()
#register_user()

connection.commit()










