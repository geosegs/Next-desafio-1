def trocar_valores(a, b):
    # trocar_valores
    a, b = b, a
    return a, b

# valores_input
a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")

# original
print(f"Valores originais - A: {a}, B: {b}")

# troca
a, b = trocar_valores(a, b)

# print
print(f"Valores trocados - A: {a}, B: {b}")