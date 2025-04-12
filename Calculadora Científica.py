import math

def mostrar_menu():
    print("\n--- CALCULADORA CIENTÍFICA ---")
    print("Operações disponíveis:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Potência (^)")
    print("6 - Raiz Quadrada (√)")
    print("7 - Seno")
    print("8 - Cosseno")
    print("9 - Tangente")
    print("10 - Logaritmo (base 10)")
    print("11 - Logaritmo Natural (ln)")
    print("12 - Fatorial (!)")
    print("13 - Constantes (π e e)")
    print("0 - Sair")

def calculadora():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma operação (0-13): ")

        if escolha == "0":
            print("Encerrando a calculadora...")
            break

        elif escolha in ["1", "2", "3", "4", "5"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                print("Resultado:", num1 + num2)
            elif escolha == "2":
                print("Resultado:", num1 - num2)
            elif escolha == "3":
                print("Resultado:", num1 * num2)
            elif escolha == "4":
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Erro: Divisão por zero!")
            elif escolha == "5":
                print("Resultado:", math.pow(num1, num2))

        elif escolha == "6":
            num = float(input("Digite o número: "))
            if num >= 0:
                print("Resultado:", math.sqrt(num))
            else:
                print("Erro: Raiz de número negativo!")

        elif escolha == "7":
            angulo = float(input("Digite o ângulo em graus: "))
            print("Seno:", math.sin(math.radians(angulo)))

        elif escolha == "8":
            angulo = float(input("Digite o ângulo em graus: "))
            print("Cosseno:", math.cos(math.radians(angulo)))

        elif escolha == "9":
            angulo = float(input("Digite o ângulo em graus: "))
            print("Tangente:", math.tan(math.radians(angulo)))

        elif escolha == "10":
            num = float(input("Digite o número (positivo): "))
            if num > 0:
                print("Log10:", math.log10(num))
            else:
                print("Erro: log só pode ser aplicado a números positivos!")

        elif escolha == "11":
            num = float(input("Digite o número (positivo): "))
            if num > 0:
                print("Log natural (ln):", math.log(num))
            else:
                print("Erro: ln só pode ser aplicado a números positivos!")

        elif escolha == "12":
            num = int(input("Digite um número inteiro não negativo: "))
            if num >= 0:
                print("Fatorial:", math.factorial(num))
            else:
                print("Erro: fatorial só é definido para inteiros não negativos!")

        elif escolha == "13":
            print("π (pi) =", math.pi)
            print("e (Euler) =", math.e)

        else:
            print("Opção inválida. Tente novamente!")

# Executa a calculadora
calculadora()
