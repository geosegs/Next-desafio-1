def calcular_desconto_e_valor(ano):
    if ano <= 2000:
        desconto = 0.12  # 12% de desconto para carros até 2000
    else:
        desconto = 0.07  # 7% de desconto para carros acima de 2000
    
    return desconto

def main():
    total_carros_ate_2000 = 0
    total_geral_carros = 0
    
    while True:
        ano = int(input("Digite o ano do veículo: "))
        valor = float(input("Digite o valor do veículo: "))
        
        desconto_percentual = calcular_desconto_e_valor(ano)
        desconto_valor = valor * desconto_percentual
        valor_com_desconto = valor - desconto_valor
        
        print(f"Desconto aplicado: {desconto_percentual * 100:.2f}%")
        print(f"Valor a ser pago: R${valor_com_desconto:.2f}")
        
        if ano <= 2000:
            total_carros_ate_2000 += 1
        
        total_geral_carros += 1
        
        continuar = input("Deseja continuar calculando desconto? (S/N) ").strip().upper()
        if continuar != "S":
            break
    
    print("\nResumo:")
    print(f"Total de carros até 2000: {total_carros_ate_2000}")
    print(f"Total geral de carros: {total_geral_carros}")

# Executar o programa
main()
