def contar_vogais(s):
    # Definir as vogais
    vogais = "aeiouAEIOU"
    
    # Inicializar o contador de vogais
    contador = 0
    
    # Percorrer cada caractere na string
    for char in s:
        if char in vogais:
            contador += 1
    
    return contador

# Solicitar a string ao usuário
string = input("Digite uma string: ")

# Contar o número de vogais na string
numero_vogais = contar_vogais(string)

# Exibir o resultado
print(f"O número de vogais na string é: {numero_vogais}")
