#Teste de senha
senha_correta ="python123"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")
    if senha != senha_correta:
        print("Senha incorreta, tente novamente.")

print("Acesso permitido! ✅")

#Até o usuário colocar 0
soma = 0
resultado = ""

while soma != 0:
    resultado = int(input("Digite um número"))

if soma != 0:
    print("tente novamente")

print("0")
