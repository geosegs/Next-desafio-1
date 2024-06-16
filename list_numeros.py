def ordenar_numeros():
    # input_lista_números_usuário_separados_espaços
    numeros_str = input("Digite uma lista de números, separados por espaços: ")
    
    # converter_string_entrada_em_lista_inteiros
    numeros = list(map(int, numeros_str.split()))
    
    # ordem_crescente 
    numeros.sort()
    
    # print_lista
    print("Lista ordenada:", numeros)

# Executar a função
ordenar_numeros()
