# 1 - função para imprimir uma mensagem

def welcome():
    print("Bem vindo ao sistema de filmes!")

# welcome()
# welcome()

# 2 - função para calcular media de notas

# def calculate_averege():
#     num_ratings = int(input("Digite a quantidade de avaliações que deseja fazer para o filme:\n"))
#     total = 0
#     for i in range(num_ratings):
#         note = float(input("Digite a nota para o filme: \n"))
#         total += note

#     if num_ratings > 0:
#         averege = total / num_ratings
#     else:
#         averege = 0

#     return averege

# print(f"A média de avaliações é: {calculate_averege():.2f}")

# 3 - Funçao para cadastrar um filme

def create_movie():
    name = input("Digite o nome do filme:\n")
    yearLaunch = int(input("Digite o ano de lançamento:\n"))
    moviePrice = float(input("Digite o preço do filme:\n"))
    rating = float(input("Digite a nota do filme:\n"))
    print(f"{name} ({yearLaunch}) - R$ {moviePrice:.2f} - Avaliação {rating:.2f}")

create_movie()
create_movie()
