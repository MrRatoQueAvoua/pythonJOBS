

num1 = float(input("Primeiro numero: "))
num2 = float(input("Segundo numero: "))
op = input("Operacao (+ - * / ): ")


if op == "+":
    resultado = num1 + num2
    print(f"O resultado e {resultado}")
elif op == "-":
    resultado = num1 - num2
    print(f"O resultado e {resultado}")
elif op == "*":
    resultado = num1 * num2
    print(f"O resultado e {resultado}")
elif op == "/":
    resultado = num1 / num2
    print(f"O resultado e {resultado}")
else:
    print("ERRO")

## codigo mais adequado seria 

# num1 = float(input("Primeiro numero: "))
# num2 = float(input("Segundo numero: "))
# op = input("Operacao (+ - * / ): ")

# if op == "+":
#     resultado = num1 + num2
#     print(f"O resultado e {resultado}")

# elif op == "-":
#     resultado = num1 - num2
#     print(f"O resultado e {resultado}")

# elif op == "*":
#     resultado = num1 * num2
#     print(f"O resultado e {resultado}")

# elif op == "/":
#     if num2 == 0:
#         print("ERRO: divisao por zero")
#     else:
#         resultado = num1 / num2
#         print(f"O resultado e {resultado}")

# else:
#     print("ERRO")
