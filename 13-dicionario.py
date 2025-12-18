filmInception = {
    "title" : "Inception",
    "yearRelease": 2010,
    "imdbRating" : 8.8,
    "genre" : ["Sci-fi", "Action", "Thriller"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

#recuperar item do dicionario
print(filmInception["genre"])
print(filmInception.get("imdbRating"))

#buscar apenas as chaves do dicionário

print(filmInception.keys())

#buscar apenas os valores
print(filmInception.values())

#buscar itens com chave e valor
print(filmInception.items())

filmInception["director"] = "Christopher Nolan"

#alterar valores
filmInception.update({"imdbRating": 8.3})

#remover item
filmInception.pop("director")