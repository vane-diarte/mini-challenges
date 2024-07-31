# Recorrido en profundidad (DFS): 
# Implementa un recorrido DFS para un grafo simple con 5 nodos.

#diccionario para representar el grafo, los nodos son las claves y los vecinos son los valores
grafo = {
    'V': ['W', 'X'],
    'W': ['V', 'Y', 'Z'],
    'X': ['V'],
    'Y': ['W'],
    'Z': ['W']

}

#funcion DFS
def dfs (grafo, nodo, visitado):
    if nodo not in visitado:
        print (nodo)
        visitado.add(nodo) #el nodo visitado se va agregando al conjunto visitado
        for vecino in grafo[nodo]:
            dfs (grafo, vecino, visitado) #se llama recursivamente a la funcion para cada vecino

visitado = set() #conjunto para guardar los nodos visitados
dfs (grafo, 'V', visitado) #llamada a la funcion dfs con el nodo inicial 'V'
