product = {
    "Arroz" : 15.50,
    "Feijão" : 8.90,
    "Macarrão" : 6.75
}

print(product)
print(max(product))
print(max(product, key=product.get))
