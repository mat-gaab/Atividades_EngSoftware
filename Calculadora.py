def calculadora():
    print("=== Calculadora Simples ===")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                return
            resultado = num1 / num2
        else:
            print("Operador inválido.")
            return

        print("Resultado:", resultado)

    except ValueError:
        print("Erro: você precisa digitar números válidos.")

calculadora()