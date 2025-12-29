# 1 - funcao de potencia de um numero

power = lambda num: num ** 2
print(power(5))

# 2 - Verifica se um numero é par

is_even = lambda x: x % 2 == 0

x = float(input("Digite o número:\n"))
if is_even(x) == True:
    print(f"O número {x} é PAR")
else:
    print(f"O número {x} é IMPAR")

# 3 - divide um numero por outro

div_num = lambda x,y : x / y

x = float(input("Digite o primeiro número:\n"))
y = float(input("Digite o segundo número:\n"))

print(f"A divisão de {x} por {y} é: {div_num(x,y)}")

#funcao que rever uma string

reverser_stg = lambda s: s[::-1]

s = input("Digite a palavra:\n")
print(reverser_stg(s))