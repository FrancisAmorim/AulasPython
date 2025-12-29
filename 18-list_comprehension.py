# # listar valores de 0 a 10 < 4
# listNumbers = [i for i in range(10) if i <4]
# print(listNumbers)

#lista de filmes
moviesList = ["Titanic", "The GodFather","Inception","Jurassic Park"]

# moviesWith = [movie for movie in moviesList if 'g' in movie.lower()]
# print(moviesWith)

# moviesWatched = [movie for movie in moviesList if input("Qual o filme?") = movie.lower()]
# print(moviesWatched)

while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar): \n")
    if searchName.lower() =="sair":
        print("Programa encerrado. Até logo!")
        break
    
    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome {searchName}:")
        for foundMovies in foundMovies:
            print(foundMovies)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente")