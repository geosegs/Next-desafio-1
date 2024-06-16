def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def determinar_mencao(media):
    if media >= 7:
        return "Aprovado"
    elif media <= 5:
        return "Reprovado"
    else:
        return "Recuperação"

def main():
    # Ler o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Ler as três notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Calcular a média aritmética
    media = calcular_media(nota1, nota2, nota3)
    
    # Determinar a menção do aluno
    mencao = determinar_mencao(media)
    
    # Exibir o nome, a média e a menção do aluno
    print(f"Nome: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Menção: {mencao}")

# Executar a função principal
main()
