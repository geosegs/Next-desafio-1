def azulejos():
    # tamanho_da_parede
    altura_parede = float(input("Escreva a altura da parede (em metros): "))
    largura_parede = float(input("Escreva a largura da parede (em metros): "))
    
    # tamanho_dos_azulejos
    altura_azulejo = float(input("Escreva a altura do azulejo (em metros): "))
    largura_azulejo = float(input("Escreva a largura do azulejo (em metros): "))
    
    # areas
    area_parede = altura_parede * largura_parede
    area_azulejo = altura_azulejo * largura_azulejo
    
    # quantidade de azulejos
    num_azulejos = (altura_parede / altura_azulejo) * (largura_parede / largura_azulejo)
    
    # quantidade certa
    import math
    num_azulejos = math.ceil(num_azulejos)
    
    # print
    print(f"O número de azulejos necessários é: {num_azulejos}")

# Executar a função
azulejos()
