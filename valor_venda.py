def calcular_valor_venda(preco_custo, percentual_acrescimo):
    # Calcular o valor do acréscimo
    valor_acrescimo = preco_custo * (percentual_acrescimo / 100)
    
    # Calcular o valor de venda
    valor_venda = preco_custo + valor_acrescimo
    
    return valor_venda

# Solicitar o preço de custo do produto ao usuário
preco_custo = float(input("Digite o preço de custo do produto: "))

# Solicitar o percentual de acréscimo ao usuário
percentual_acrescimo = float(input("Digite o percentual de acréscimo: "))

# Calcular o valor de venda
valor_venda = calcular_valor_venda(preco_custo, percentual_acrescimo)

# Exibir o valor de venda
print(f"O valor de venda do produto é: R${valor_venda:.2f}")
