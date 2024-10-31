# Passo 1: Receber uma entrada do usuário
frase = input("Digite uma palavra ou frase: ")  # Pedimos ao usuário para digitar algo

# Passo 2: Limpar a frase
frase_limpa = ''.join(caractere.lower() for caractere in frase if caractere.isalnum())
# Aqui, removemos espaços e deixamos tudo minúsculo, guardando apenas letras e números

# Passo 3: Verificar se é um palíndromo
if frase_limpa == frase_limpa[::-1]:  # Verificamos se a frase limpa é igual ao seu inverso
    print("É um palíndromo!")  # Se sim, é um palíndromo
else:
    print("Não é um palíndromo.")  # Senão, não é um palíndromo
