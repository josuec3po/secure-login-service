import bcrypt

print("===== RANDOM WEBSITE LOGIN =====")

login = str(input("Login: "))

senha = str(input("Senha: ")).encode('utf-8')

'''
### METODO DE ENCODING
O UTF-8 é o padrão dominante de codificação de caracteres na web, 
mapeando caracteres Unicode para sequências de 1 a 4 bytes, 
garantindo compatibilidade com ASCII.
'''
hashed = bcrypt.hashpw(senha, bcrypt.gensalt(rounds=12))

print(hashed)

if bcrypt.checkpw(senha, hashed):
    print("Combinam")
else:
    print("Não combinam")
   

