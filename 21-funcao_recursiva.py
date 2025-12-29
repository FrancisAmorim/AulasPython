#Fatorial de um numero

def factorial (num):
    if num == 1:
        return 1
    else:
        return (num * factorial (num -1))
number = int(input("Digite o número para o fatorial:\n"))
print(f"O fatorial de {number} é {factorial(number)}")

# soma total de um numero com seus antecessores

def total_sum (num):
    if num == 1:
        return 1
    else:
        return(num + total_sum(num -1))
    
num  = int(input("Digite o número para somar seus antecessores:\n"))
print(f"A soma do numero {num} com seus antecessores é {total_sum(num)}")