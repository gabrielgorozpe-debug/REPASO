from clases.herencia1.animales import Animal


class Gato(Animal):

    def __init__(self, especie, nombre, velocidad):
        super().__init__(especie, nombre)
        self.velociad = velocidad

    def __str__(self):
        return super().__str__() +""+ str(self.velociad)

    def maullar(self):
        print("gato haciendole miau")