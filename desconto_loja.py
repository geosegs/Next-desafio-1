def calcular_total():
    # input_descrição
    nome_produto = input("Digite a descrição do produto: ")
    
    # input_quantidade
    quantidade = int(input("Digite a quantidade coletada: "))
    
    # input_preçounitário
    preco_unitario = float(input("Digite o preço unitário: "))
    
    # calcular_total
    total = quantidade * preco_unitario
    
    # desconto
    if quantidade <= 5:
        desconto = 0.02 * total
    elif quantidade <= 10:
        desconto = 0.03 * total
    else:
        desconto = 0.05 * total
    
    # calcular_total_pagar
    total_a_pagar = total - desconto
    
    # print_resultados
    print(f"Descrição do produto: {nome_produto}")
    print(f"Quantidade adquirida: {quantidade}")
    print(f"Preço unitário: R${preco_unitario:.2f}")
    print(f"Total: R${total:.2f}")
    print(f"Desconto: R${desconto:.2f}")
    print(f"Total a pagar: R${total_a_pagar:.2f}")

# Executar a função
calcular_total()
