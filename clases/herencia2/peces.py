from clases.herencia1.animales import Animal

class Pez(Animal):

    def __init__(self, especie, nombre, aletas):
        super().__init__(especie, nombre)
        self.aletas = aletas

    def __str__(self):
        return super().__str__() +" "+self.aletas
    
    def nadar(self):
        print("Pez nadando") 