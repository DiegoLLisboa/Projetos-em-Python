def adicionar(x, y):
    return x + y
def subtrair(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    return x / y
def mostrar_menu():
    print("\nSelecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    mostrar_menu()

    # Entrada do usuário
    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha == '5':
        print("Obrigado por usar a calculadora. Até mais!")
        break

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")
            continue

        if escolha == '1':
            print(f"Resultado: {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif escolha == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {resultado}")

    else:
        print("Escolha inválida! Por favor, escolha uma opção válida.")
