import csv
import json

'''
# Crie um programa que grave uma lista de nomes em um arquivo de texto e depois leia-os de volta.
soma = 0
with open("exercicio01.txt", "w") as f:
    f.write("Sarah\n")
    f.write("Ewerson\n")
    f.write("Lucas\n")

with open("exercicio01.txt", "r") as f:
    for linha in f:
        print(linha.strip())    

'''

'''
# Escreva um programa que crie um arquivo notas.txt com as notas dos alunos (10 alunos) e depois as imprima linha por linha.

alunos = {
    "aluno1": 9, "aluno2": 5.6, "aluno3": 4.5, "aluno4": 2, "aluno5": 10,"aluno6": 7, "aluno7": 4.9, "aluno8": 19, "aluno9": 8, "aluno10": 5
}

with open("alunos_notas.txt", "a") as f:
    for aluno, nota in alunos.items():
        print(f'{aluno} -> {nota}', file=f)
'''

'''
# Faça um programa que leia as notas do arquivo informado e calcule a média de notas

quantidade_alunos = 0 
soma_notas = 0
 
with open("alunos_notas.txt", "r") as f:
    for linha in f:
        quantidade_alunos +=1 
        soma_notas += float(linha.split(' -> ')[1])

if quantidade_alunos !=0:
    media = soma_notas/quantidade_alunos
    print(f"Media = {media}")
else:
    print("Nenhuma nota foi encontrada no arquivo")
'''

'''
# Crie um programa que conte o número de linhas de um arquivo de texto.
soma = 0 
with open('exemplo_arquivo.txt', "r") as f:
    for linha in f:
        soma += 1
print(soma)
'''

'''
# Faça um programa que leia um arquivo e mostre apenas as linhas que começam com a letra “A”.
with open("exemplo_arquivo.txt", 'r') as f:
    for linha in f:
        if linha.startswith('A'):
            print(linha.strip())
'''

'''
with open("dados.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["nome", "idade"])
    writer.writerow(["Ana", 25])
    writer.writerow(["João", 30])
    
with open("dados.csv", "r") as f:
    reader = csv.reader(f)
    for linha in reader:
        print(linha)


with open("banco.csv", "w", newline="") as f:
    escrever = csv.writer(f)
    escrever.writerow(["nome", "idade", "cidade"])
    escrever.writerow(["sarah", 20, "maceio"])
    
with open("banco.csv", "r") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)

dados = {"nome": "sarah", "idade": 28, "cidade": "maceio"}
with open("dados.json", "w") as f:
    json.dump(dados,f)
with open("dados.json", "r") as f:
    info = json.load(f)
    print(info)
'''

'''
# Crie um arquivo CSV com nomes e idades, depois leia e imprima apenas pessoas maiores de 18 anos.
with open("nome_idade.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sarah", 20])
    writer.writerow(["lucas", 19])
    writer.writerow(["luiz", 21])
    writer.writerow(["samanta", 10])
    writer.writerow(["sara", 18])
    writer.writerow(["dennis", 17])
    writer.writerow(["luiza", 14])
    writer.writerow(["manuela", 11])
    writer.writerow(["marta", 15])
with open("nome_idade.csv", "r") as f:
    reader = csv.reader(f)
    for nome, idade in reader:
        if int(idade) > 18:
            print(f"{nome} - {idade}")
'''

'''
# Grave em JSON as informações de um produto (nome, preço, quantidade) e leia de volta mostrando em formato legível.
produto = {
    "nome": "bolo", "preço": 19.5, "quantidade": 150}
with open("produtos.json", "w") as f:
    json.dump(produto, f)
with open("produtos.json", "r") as f:
    dados = json.load(f)
    for key, value in dados.items():
        print(f"{key}: {value}")
'''