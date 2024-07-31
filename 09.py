# Eliminar duplicados: 
# Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.


def eliminar_duplicados(lista):
    return list(set(lista)) 
# la clase list convierte el conjunto en una lista
# set es un conjunto que no permite duplicados

lista = [1, 2, 3, 4, 5, 6, 5, 1, 6, 7]
sin_duplicados = eliminar_duplicados(lista) 

print("Lista original:", lista)
print("Lista sin duplicados:", sin_duplicados)