def saudacao():
    print('Olá, mundo!')

saudacao()


def saudacao_personalizda(nome):
    print('Olá,', nome)

saudacao_personalizda('João')


def soma(n1, n2):
    resultado = n1 + n2
    return resultado

total = soma(10, 20)
print(total)


def somar (x, y):
    return x + y

def subtrair (x, y):
    return x - y

def multiplicar (x, y):
    return x * y

def dividir (x, y):
    if y == 0:
        return "Não é possível dividir por zero"
    else:
        return x / y
    

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Operações disponíveis: ")    
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite o número da operação desejada (1/2/3/4): ")

if escolha == '1':
    print(num1, '+', num2, '=', somar(num1, num2))
elif escolha == '2':
    print(num1, '-', num2, '=', subtrair(num1, num2))
elif escolha == '3':
    print(num1, '*', num2, '=', multiplicar(num1, num2))
elif escolha == '4':
    print(num1, '/', num2, '=', dividir(num1, num2))
else:
    print("Operação inválida")