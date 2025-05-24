'''Crie um programa que:
- Permita ao usuário cadastrar 3 filmes que ele assistiu recentemente.
- Para cada filme, peça:
    • O título do filme
    • A nota que o usuário dá de 0 a 10
- Guarde essas informações em uma lista aninhada (cada filme é uma sublista com título e nota).
- Ao final, exiba todos os filmes com sua respectiva nota, e destaque quais receberam nota maior ou igual a 8 como "Recomendado!".'''

filmes = []

for i in range(3):
    titulo = input(f"Digite o título do filme {i+1}: ")
    nota = float(input(f"Digite a nota para '{titulo}' (0 a 10): "))
    filmes.append([titulo, nota])

print("\nFilmes assistidos:")
for titulo, nota in filmes:
    status = " - Recomendado!" if nota >= 8 else ""
    print(f"{titulo} (Nota: {nota}){status}")
