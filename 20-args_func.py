# 1 - função para imprimir um nome completo

def full_name (first_name, last_name):
    print(f"Nome:{first_name} {last_name}")

full_name("Fulano","Sicrano")

# 2 - Funçao para somar 2 numeros

def sum_numbers (a, b):
    return a + b

print(F"Soma é {sum_numbers(50,10)}")

# 3 - Função com parametro default

def address (country="Brasil"):
    print(f"Eu moro em : {country}")

address()

# 4 - Funçao para avaliar um filme

def rate_movie(movie_name, num_ratings):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme: \n"))
        total += note

        if num_ratings > 0:
            averege = total / num_ratings
    else:
        averege = 0

    print(f"Média de avaliação  do filme: {movie_name} é: {averege:.2f}")

rate_movie(2, "Sonic")