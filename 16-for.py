#lista de filmes

moviesList = ["Titanic", "The GodFather","Inception","Jurassic Park"]
# 1- iterando valores de uma lista

for movie in moviesList:
    print(movie)

for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)

for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)

#4 - avaliação do filme:

movieName = input("Digite o nome do filme: \n")    
movieRating = int(input("Digite a quantidade de avaliações: \n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota do filme:\n"))
    total += note

if movieRating >0:
    average = total / movieRating
else:
    average = 0

print (f"Média de avaliações do filme {movieName} é: {average:.2f}")
