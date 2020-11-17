"""
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
"""

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivelCombustivel = 0

    def Andar(self, distancia):
        temp = distancia / self.consumo
        self.nivelCombustivel -= temp

    def obterGasolina(self):
        return self.nivelCombustivel

    def adicionarGasolina(self, quantidade):
        self.nivelCombustivel += quantidade

veiculo = input("Qual é seu carro?: ")
consumo = int(input(f"Digite o consumo de combustivel do carro {veiculo}: "))
meu_carro = Carro(consumo)
quantidade = int(input("Digite quanto de gasolina quer adicionar: "))
meu_carro.adicionarGasolina(quantidade)
distancia = int(input("Digite a distancia percorrida: "))
meu_carro.Andar(distancia)
print(meu_carro)
print(meu_carro.obterGasolina())