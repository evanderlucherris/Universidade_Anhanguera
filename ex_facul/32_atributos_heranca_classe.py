class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        # Carros podem acelerar mais rápido.
        self.velocidade += incremento + self.potencia

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} km/h"

# Criando objetos
carro1 = Carro(f"Toyota", "Corolla", 2022, 150)
bicicleta1 = Bicicleta(f"Trek", "Mountain Bike", 2021, "MTB")

# Acelerando e verificando o status
carro1.acelerar(50)
bicicleta1.acelerar(20)

# Exibindo o status dos veículos
print("Status do Carro:")
print(carro1.status())

print("\nStatus da Bicicleta:")
print(bicicleta1.status())