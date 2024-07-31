# Búsqueda en lista ordenada: 
# Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos.

lista_ordenada = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]


numero_usuario = int (input ('ingrese un numero '))

def numero_en_lista ():
    encontrado = False
    for i in lista_ordenada:
        if i == numero_usuario:
            encontrado = True
            break

    if encontrado:
        print (f'El numero {numero_usuario}, se encuentra en la lista')
    else:
        print ('El numero no se encuentra en la lista')

numero_en_lista()

