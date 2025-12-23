moviesList = ["Titanic", "The GodFather","Inception","Jurassic Park"]

#1- interando valores de uma lista de files usando while

# index = 0
# while index < len(moviesList):
#     print(moviesList[index])
    # index +=1

#2- quando a condição for atendida o loop para 

index = 0
while index < len(moviesList):
    if moviesList [index] == "Inception":
        break
    print(moviesList[index])
    index +=1

#3- quando a condição for atendida passa para o próximo
# 
index = 0
while index < len(moviesList):
    if moviesList [index] == "Inception":
        index +=1
        continue
    print(moviesList[index])
    index +=1    