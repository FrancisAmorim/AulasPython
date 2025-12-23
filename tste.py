# testando aprendizado do for e while

moviesList = ["Vingadores","O Livro de Eli","Titanic","A Origem","Mudança de Hábito"]

#Criando loop for para teste

nomeAluno = input("Digite o nome do aluno: \n")
quantidadeNotas = int(input("Digite quantas notas serão consideradas: \n"))

totalNotas = 0
for i in range (quantidadeNotas):
    notas = float(input(f"Digite a {i+1}ª nota:\n"))
    totalNotas += notas

if quantidadeNotas > 0:
    mediaAluno = totalNotas / quantidadeNotas
else:
    mediaAluno = 0

if mediaAluno >= 6:
    print(f"O aluno {nomeAluno} foi aprovado com a média {mediaAluno:.2f} ===Parabéns===")
else:
    print(f"Aluno {nomeAluno} REPROVADO. Média: {mediaAluno}")