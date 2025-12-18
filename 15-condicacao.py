# #informaçõe sobre o filme
# name = input("digite o nome do filme: \n")
# yearRelease = int(input("digite o ano de lançamento: \n"))
# rating = float(input("digite a nota do filme: \n"))

# #verifica se o filme é recomendado

# if rating > 8.0 and yearRelease > 2015:
#     print(f"o filme {name} é muito bom. Recomendo assisti-lo. Nota: {rating}")
# else:
#     print(f"o filme {name} ainda nao atingiu uma boa nota. Nota: {rating}")


num1 = float(input("Digite o primeiro numero: \n"))
num2 = float(input("Digite o segundo numero: \n"))
operador = input("digite a operação: (+ - * /) \n")

if operador == "+":
    result = num1 + num2
elif operador == "-":
    result = num1 - num2
elif operador == "*":
    result = num1 * num2
elif operador == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por zero")
        result = "#ERRO"
else:
    print("operação invalida")
    result = 0

if result =="#ERRO":
    print(f"O resultado da operação é: {result}")
else:
    print(f"O resultado da operação é: {result:.2f}")
