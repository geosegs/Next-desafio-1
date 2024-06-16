def calcular_reajuste(salario, salario_minimo):
    if salario < 3 * salario_minimo:
        reajuste = salario * 0.50
    elif 3 * salario_minimo <= salario <= 10 * salario_minimo:
        reajuste = salario * 0.20
    elif 10 * salario_minimo < salario <= 20 * salario_minimo:
        reajuste = salario * 0.15
    else:
        reajuste = salario * 0.10
    return salario + reajuste

def main():
    # Definir o valor do salário mínimo
    salario_minimo = float(input("Digite o valor do salário mínimo: "))
    
    # Inicializar a lista de salários
    salarios = []

    # Solicitar os salários dos 584 funcionários
    for i in range(584):
        salario = float(input(f"Digite o salário do funcionário {i+1}: "))
        salarios.append(salario)
    
    # Calcular e exibir os salários reajustados
    for i, salario in enumerate(salarios):
        salario_reajustado = calcular_reajuste(salario, salario_minimo)
        print(f"Funcionário {i+1}: Salário original: R${salario:.2f}, Salário reajustado: R${salario_reajustado:.2f}")

# Executar a função principal
main()
