def verificar_maioridade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"

def main():
    # começr_lista_idades
    idades = []

    # loop_ler_idade_75_pessoas
    for i in range(1, 76):
        idade = int(input(f"Digite a idade da pessoa {i}: "))
        idades.append(idade)

    # maioridade_cada_pessoa_exibir_mensagem
    for i, idade in enumerate(idades):
        status = verificar_maioridade(idade)
        print(f"Pessoa {i+1} é {status}.")

# Executar a função principal
main()
