def media_escola():
  while True:
      # notas input
      nota1 = float(input("Escreva a nota do primeiro bimestre: "))
      nota2 = float(input("Escreva a nota do segundo bimestre: "))
      nota3 = float(input("Escreva a nota do terceiro bimestre: "))
      nota4 = float(input("Escreva a nota do quarto bimestre: "))

      # calculo
      media = (nota1 + nota2 + nota3 + nota4) / 4

      # média
      print(f"A média bimestral é: {media:.2f}")

      # continuar ou não
      continuar = input("Deseja continuar (S/N)? ").strip().upper()
      if continuar != 'S':
          print("Encerrando o programa.")
          break

# Executar a função
media_escola()
