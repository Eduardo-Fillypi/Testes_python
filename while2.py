# código que eu fiz
regressiva = 1
numero_inicial = ''

while numero_inicial != regressiva:
    numero_inicial = int(input('Digite um número'))

if regressiva != 1:
    numero_inicial -= -1

# código correto

numero = int(input("Digite um número para iniciar a contagem regressiva: "))

while numero >= 1:
    print(numero)
    numero -= 1  # diminui 1 a cada repetição

print("Contagem finalizada!")

# terceiro código

palavra = input('Digite uma palavra:')
palavra_certa = 'sair'

while palavra_certa == palavra:
    print('tente novamente')

print('Sucesso')

# quarto código 

palavra = ''
continuar = "sim"
parar = "não"
while palavra == continuar:
    palavra = input('Digite sim para continuar e não para finalizar')

if palavra == parar:
    print('Programa finalizado com sucesso')

# quinto código 

numero = 0

while numero != 10:
    numero = int(input('Digite um número'))

print('Parabéns')

# sexto codigo

palavra = ""

while palavra != "python":
    palavra = input("Digite a palavra secreta: ")

print("Parabéns, você acertou a palavra!")

# sétimo codigo

cor = ''

while cor != "azul":
    cor = input("digite uma cor:  ")

print('Parabéns, você acertou!!')

# oitavo codigo 

numero = 0

while numero != 7:
    numero = int(input('Digite um número:  '))

print('Programa encerrado')
