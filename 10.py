class Punto2D:
    def __init__(self, x, y):
     
        self.x = x
        self.y = y

    def imprimir_coordenadas(self):
        print(f"Coordenadas: ({self.x}, {self.y})")

def obtener_coordenadas():
    try:
        x = int(input("Ingrese la coordenada x: "))
        y = int(input("Ingrese la coordenada y: "))
        return x, y
    except ValueError:
        print("Por favor, ingrese valores enteros")
        return obtener_coordenadas()

x, y = obtener_coordenadas()
punto = Punto2D(x, y)
punto.imprimir_coordenadas()


