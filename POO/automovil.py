class Automovil:

    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def Avanzar(self):
        print(f"El auto avanza y es de la marca: {self.marca}")

    def Retroceder(self):
        print(f"El auto retrocede y es de color: {self.color}")




if __name__ == "__main__":

    auto1 = Automovil("BMW","Rojo")
    auto1.Avanzar()
    auto1.Retroceder()


    