def processar_numeros():
    # Inicializar a lista para armazenar os números
    numeros = []

    # Solicitar os 10 números inteiros ao usuário
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)

    # Inicializar variáveis para a multiplicação dos pares e soma dos ímpares
    multiplicacao_pares = 1
    soma_impares = 0

    # Processar a lista de números
    for numero in numeros:
        if numero % 2 == 0:
            multiplicacao_pares *= numero
        else:
            soma_impares += numero

    # Exibir os resultados
    print(f"Multiplicação dos números pares: {multiplicacao_pares}")
    print(f"Soma dos números ímpares: {soma_impares}")

# Executar a função
processar_numeros()
