# Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, 
# escribe una función que encuentre el camino más corto entre dos nodos especificados usando cualquier método que prefieras.

from queue import Queue #importamos la clase Queue del modulo queue

#diccionario para representar el grafo, los nodos son las claves y los vecinos son los valores
grafo = {
    'V': ['W', 'X'],
    'W': ['V', 'X', 'Y'],
    'X': ['V', 'Z'],
    'Y': ['W', 'Z'],
    'Z': ['Y', 'X']
}
def bfs (grafo, origen, final):
    visitado = set ([origen]) #marcamos como visitado el origen
    cola = Queue()

    #añadimos a la cola una tupla con el nodo inicial y una lista con el camino inicial (el nodo origen)
    cola.put((origen, [origen])) 
    while not cola.empty():
        nodo_actual, camino = cola.get() #extraemos de la cola el nodo actual y el camino
        if nodo_actual == final:
            return camino
        
        for vecino in grafo[nodo_actual]:
            if vecino not in visitado:
                visitado.add (vecino)

                nodo_siguiente = vecino
                nuevo_camino = camino +[nodo_siguiente] #concatenamos la lista que contiene el camino con la del nodo siguiente que seria el vecino
                nodo_camino = (nodo_siguiente, nuevo_camino ) #empaquetamos el vecino y el nuevo camino en una tupla
                cola.put(nodo_camino) #Agregamos el nodo y su camino a la cola
    
    # Si no se encuentra ningún camino
    return None


camino_corto = bfs (grafo, 'V', 'Z')
print (camino_corto)


    
