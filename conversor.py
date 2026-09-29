def conversor():
    print("=== Conversor de Temperatura ===")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    
    opcao = input("Escolha a opção (1 ou 2): ")
    if opcao == '1':
        c = float(input("Digite °C: "))
        print(f"Resultado: {(c * 9/5) + 32:.2f}°F")
    elif opcao == '2':
        f = float(input("Digite °F: "))
        print(f"Resultado: {(f - 32) * 5/9:.2f}°C")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    conversor()
