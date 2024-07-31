#Recorrido en amplitud (BFS): 
# Implementa un recorrido BFS para un grafo simple con 5 nodos.

from queue import Queue #importamos la clase Queue del modulo queue

#diccionario para representar el grafo, los nodos son las claves y los vecinos son los valores
grafo = {
    'V': ['W', 'X'],
    'W': ['V', 'Y', 'Z'],
    'X': ['V'],
    'Y': ['W'],
    'Z': ['W']
}

#funcion BFS
def bfs (grafo, origen):
    visitado = set() #conjunto para guardar nodos visitados
    cola = Queue() #creamos una cola
    cola.put(origen) #añadimos el origen a la cola
    
    while not cola.empty(): #mientras la cola no este vacia
        nodo_actual = cola.get() # extraemos el nodo de la parte frontal de la cola
        if nodo_actual not in visitado:
            print(nodo_actual)
            visitado.add(nodo_actual) #agregamos el nodo actual al conjunto de visitados
            for vecino in grafo[nodo_actual]: #iteramos en los vecinos del nodo actual
                if vecino not in visitado:
                    cola.put(vecino) #agregamos el vecino a la cola
                    
bfs (grafo, 'V') #llamada a la funcion dfs con el nodo inicial 'V'

        

