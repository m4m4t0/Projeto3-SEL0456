from hashlib import sha256

# abre os arquivos com a senha correta e a senha criptografada
with open("senha_correta.txt", "r") as senha_txt:
    senha = senha_txt.read()
with open("senha_criptografada.txt", "r") as criptografia_txt:
    senha_C = criptografia_txt.read()

# obtem o hash em hexadecimal da senha
hash_senha = sha256(senha.encode()).hexdigest()

# compara o hash da senha com o hash informado pelo arquivo "senha_criptografada.txt"
if hash_senha == senha_C:
    print(f"'{senha}' é uma senha válida.")
else:
    print(f"'{senha}' não é a senha correta!")

# tratamento para pytest
'''def resultado():
    asset hash_senha == senha_C'''