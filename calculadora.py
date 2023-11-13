def calculadora(num1, num2, num_operacao):
    if (num_operacao == 1): return num1 + num2
    elif (num_operacao == 2): return num1 - num2
    elif (num_operacao == 3): return num1 * num2
    elif(num_operacao == 4): return num1 / num2
    else: return 0
""" num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")
num_operacao = input("Insira a aoperação matemática: 1 Soma / 2 Subtração / 3 Multiplicação / 4 Divisão: ")
int(num_operacao) """

num1 = 2
num2 = 31
num_operacao = 4
resultado = calculadora(num1, num2, num_operacao)
print(resultado)