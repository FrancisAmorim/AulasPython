#slice ou fatiamento
movieName = "Top Gun"

#string[inicio:fim] - indice começa na posição 0 | índice final - 1

# 1 - Bucar toda a string a partir da primeira posição

print(movieName[0:])

# toda a string até a ultima posição

print(movieName[:7])

# buscar toda string da terceira até a ultima

print(movieName[2:])


"""
string[inicio:fim:passo]
indice começa na posição 0 | indice final -1
passo - determina o incremento. por padrão esse numero é o 1.
"""

# 4 - Buscar toda a string de 2 em 2 caracteres

print(movieName[::2])

# 5 - Buscar toda a string nos indices impares

print(movieName[1::2])

# 6 - inverter uma string

print(movieName[::-1])

