def eh_palindromo(s):
    # Remover espaços em branco e converter para minúsculas
    s = s.replace(" ", "").lower()
    
    # Verificar se a string é igual ao seu reverso
    if s == s[::-1]:
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"

# Solicitar a string ao usuário
string = input("Digite uma string: ")

# Verificar se a string é um palíndromo e exibir o resultado
resultado = eh_palindromo(string)
print(resultado)
