from clases.herencia2.peces import Pez
from clases.herencia2.perros import Perro
from clases.herencia2.gatos import Gato

def main():

    pz = Pez("payaso","nemo","con defecto")

    print(pz)

    pz.respirar()
    pz.nadar()


    pr = Perro("yaqui","cooper",1000)
    print(pr)
    pr.respirar()
    pr.ladrar()


    gt = Gato("persa","garfiel",60)
    print(gt)
    gt.respirar()
    gt.maullar()

if __name__ == "__main__":
    main()
