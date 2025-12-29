"""
*args - utilizamos ele quando nao temos certeza de quantos argumentos queremos ter numa função.
 - os argumentos sao passados como uma tupla
**kwarg - alem dos valores podemos passar tambem as respectivas chaves para cada argumento
-- passados no formato de dicionario

"""
#soma de numeros 

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(7,10)

# - 2 apresntação de cursos

def presentation (**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista de cursos")
presentation(name="Python" , Category="Backend" , level="Iniciante")
presentation(name="visão computacional com python" , Category="IA" , level="avançado")
presentation(name="Dashboards com Dash" , Category="Data Science" , level="Intermediário")
