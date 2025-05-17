import random

print("Entero Aleatorio entre 0 y 6:", random.randint(0, 6))

lista = [1, 2, 3, 4, 5]
print("Elemento Aleatorio de la lista:", random.choice(lista))

#Barajar una lista
print(f"Lista Original: {lista}")
random.shuffle(lista)
print("Lista Barajada:", lista)

caras_dados = [1,2,3,4,5,6]
#Simular 100 tiradas de dados
for _ in range(0,99):
    print(f"Lanzar un dado Cara: {random.choice(caras_dados)}")