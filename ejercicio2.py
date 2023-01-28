from pickle import *

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, color: {self.color}"


vehiculo = Vehiculo("Toyota", "Auris", "rosado")



file = open('vehiculo_objeto', 'w+b')

dump(vehiculo, file)

file.seek(0)
nuevo_vehiculo = load(file)

print(nuevo_vehiculo)

