# Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.

class Nodo: #creamos la clase nodo
    def __init__(self, valor): #le pasamos como argumento el valor
        self.valor = valor
        self.siguiente = None #enlace al siguiente nodo

class Pila:
    def __init__(self):
        self.cabeza = None #inicia con la cabeza vacía

    def push(self, valor): #inserta un elemento en la parte superior de la pila
        
        nuevo_nodo = Nodo(valor) #creamos un objeto con la clase nodo
        nuevo_nodo.siguiente = self.cabeza #el nuevo nodo siguiente apunta a la cabeza
        self.cabeza = nuevo_nodo #actualiza la cabeza de la pila con el valor del nuevo nodo

    def pop(self): #Elimina y devuelve el elemento superior de la pila.
        if self.is_empty(): #si la pila esta vacía
            raise IndexError ("Error, la pila esta vacia")
        
        nodo_a_eliminar = self.cabeza #se coloca el primer elemento de la pila como nodo a eliminar
        self.cabeza = self.cabeza.siguiente #se actualiza el nodo cabeza con el valor del nodo que le sigue
        return nodo_a_eliminar.valor
    
    def peek (self):
        if self.is_empty():
            raise IndexError("La pila esta vacia")
        return self.cabeza.valor
    
    def is_empty(self):
        return self.cabeza is None
    
    def imprimir_pila(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente
    

    
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)



#pila.pop()
# print(pila.peek())


print("pila:")
pila.imprimir_pila()




