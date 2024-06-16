def calcular_custo_consumidor(custo_fabrica):
    # fixos
    percentual_impostos = 45 / 100
    percentual_distribuidor = 28 / 100

    # valor_imposto
    valor_impostos = custo_fabrica * percentual_impostos
    
    # custo_dps_do_imposto
    custo_apos_impostos = custo_fabrica + valor_impostos
    
    # valor_distribuidor
    valor_distribuidor = custo_apos_impostos * percentual_distribuidor
    
    #custo_do_consumidor
    custo_consumidor = custo_apos_impostos + valor_distribuidor
    
    return custo_consumidor

# input_custo_fábrica_carro
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

# calcular_custo_consumidor
custo_consumidor = calcular_custo_consumidor(custo_fabrica)

# print_consumidor
print(f"O custo ao consumidor do carro é: R${custo_consumidor:.2f}")
