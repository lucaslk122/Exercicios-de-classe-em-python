"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""

class Macaco:
    def __init__(self,nome):
        self.nome = nome
        self.bucho = []

    def Comer(self, comida):
        self.bucho.append(comida)

    def VerBucho(self):
        print(f"Bucho: {self.bucho}")

    def digerir(self):
        if len(self.bucho) > 0:
            self.bucho.pop(0)

nome_macaco1 = input("Digite o nome do macaco 1: ")
nome_macaco2 = input("Digite o nome do macaco 2: ")
m1 = Macaco(nome_macaco1)
m2 = Macaco(nome_macaco2)
comer1 = input(f"O que o macaco {nome_macaco1} vai comer?: ")
comer2 = input(f"O que o macaco {nome_macaco2} vai comer?: ")
m1.Comer(comer1)
m2.Comer(comer2)


