import random

# Crie uma lista vazia chamada frutas e adicione nela, nesta ordem, as seguintes frutas: "maçã", "banana" e "laranja"
frutas = []
frutas.append("maçã")
frutas.append("banana")
frutas.append("laranja")
print(frutas)

# Na lista numeros = [1, 2, 4, 5], insira o número 3 na posição correta para manter a sequência numérica.
numeros = [1, 2, 4, 5] 
numeros.insert(2, 3)
print(numeros)

# Dada a lista itens = ["teclado", "mouse", "monitor", "mouse"], remova apenas o primeiro item "mouse" da lista.
itens = ["teclado", "mouse", "monitor", "mouse"]
itens.remove("mouse")

# Verifique se a string "carro" está presente na lista veiculos = ["moto", "bicicleta", "carro", "ônibus"]. Imprima uma mensagem apropriada.
veiculos = ["moto", "bicicleta", "carro", "ônibus"]
if "carro" in veiculos:
  print("Carro está presente na lista")
else:
  print("Carro não está presente na lista")
  
# Dada a lista nomes = ["Ana", "Beatriz", "Carlos"], remova o último elemento da lista usando um método apropriado e armazene o valor removido em uma variável chamada removido.
nomes = ["Ana", "Beatriz", "Carlos"]
removido = nomes.pop()
print(f"Nome removido: {removido}")

# Crie uma lista com 50 elementos randômicos, ordene a lista in-place e imprima a nova lista:
aleatorios = []

while len(aleatorios) <= 50:
  aleatorios.append(random.randint(1, 100))
  
print(f"Lista não ordenada: {aleatorios}")
aleatorios.sort()
print(f"Lista ordenada: {aleatorios}")

  
