# Usando list comprehension, crie uma lista com as letras da palavra "informática" exceto as vogais.
palavra = "informática"
vogais = ["a", "á", "e", "i", "o", "u"]
consoantes = [x for x in palavra if x not in vogais]
print(consoantes)

# Dada a matriz matriz = [[1, 2], [3, 4], [5, 6]], crie uma lista achatada com todos os elementos da matriz.

# Dada a lista valores = [3, -2, 7, -1, 0], crie uma nova lista onde números negativos são substituídos por 0 e os demais permanecem inalterados.
valores = [3, -2, 7, -1, 0]
for i in range(len(valores)):
 if valores[i] < 0:
    valores[i] = 0
print(valores)

# Dada a string "a1b2c3d4", use list comprehension para criar uma lista com os números inteiros extraídos da string.
caracteres = "a1b2c3d4" 
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
inteiros = [x for x in caracteres if x in numeros]

# Dada a lista numeros = list(range(20)), crie uma nova lista contendo o dobro de todos os números ímpares maiores que 5 e menores que 20.
numeros = list(range(20))
dobro = [x * 2 for x in numeros if x % 2 != 0 and 5 < x < 20]
