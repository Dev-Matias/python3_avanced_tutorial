#Crea una clase `Rectangulo` con métodos para calcular su área y perímetro.  
#self referencia a la instancia actual de la clase y se utiliza para acceder a los atributos y métodos de la clase.
class Rectangulo:
    def __init__(self, base, altura):# Constructor
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
# Crear un objeto de la clase Rectangulo
rectangulo = Rectangulo(5, 10)
# Mostrar el área y el perímetro
print("Área del rectángulo:", rectangulo.area())
print("Perímetro del rectángulo:", rectangulo.perimetro())
