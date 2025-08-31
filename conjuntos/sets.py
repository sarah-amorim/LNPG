'''
1. Remover duplicatas de uma lista
    Dada a lista numeros = [1, 2, 2, 3, 4, 4, 5], use um set para
    remover os elementos duplicados e exiba o resultado.
'''
numeros = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(numeros)
print(conjunto)

'''
2. Encontrar elementos em comum
    Considere duas listas:
    alunos_manha = ["Ana", "Pedro", "Lucas", "Maria"]
    alunos_tarde = ["Maria", "Paulo", "Lucas", "Joana"]
Use conjuntos para encontrar quais alunos estudam nos dois turnos.
'''
alunos_manha = set(["Ana", "Pedro", "Lucas", "Maria"])
alunos_tarde = set(["Maria", "Paulo", "Lucas", "Joana"])

dois_turnos = alunos_manha & alunos_tarde
print(f"Alunos que estudam nos dois turnos: {dois_turnos}")

'''
3. Encontrar elementos exclusivos
    Usando os mesmos conjuntos da questão anterior, encontre os alunos
    que estudam apenas de manhã ou apenas à tarde, mas não em ambos
    (diferença simétrica).
'''
manha_tarde = alunos_manha ^ alunos_tarde
print(f"Alunos que estudam apenas de manhã ou apenas à tarde: {manha_tarde}")

'''
4.  Checar pertinência rapidamente
    Crie um conjunto com os números de 1 a 1000. Depois, peça para o usuário digitar um 
    número e verifique se ele está no conjunto.
'''
nums = set([x for x in range(1, 1001)])
digito = int(input("Digite um número para verificar se está no conjunto: "))

if digito in nums:
    print(f"{digito} está no cojunto")
else:
    print(f"{digito} não está no cojunto")

'''
5. Operações matemáticas de conjuntos
    
    Dados os conjuntos:
    primos = {2, 3, 5, 7, 11, 13}
    pares  = {2, 4, 6, 8, 10, 12}

    Encontre os números que são primos e pares.
    Encontre os números que são primos ou pares.
    Encontre os números que são pares mas não primos.
'''
primos = {2, 3, 5, 7, 11, 13}
pares  = {2, 4, 6, 8, 10, 12}

print(f"Números que são primos e pares {primos & pares}")
print(f"Números que são primos ou pares {primos | pares}")
print(f"Números que são pares mas nao primos {pares - primos}")