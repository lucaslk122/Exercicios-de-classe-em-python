"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""

import random

class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setfome(fome)
        self.setsaude(saude)
        self.setidade(idade)

    def setNome(self, nome):
        self.nome = nome

    def setfome (self, fome):
        self.setfome = fome

    def setidade (self, idade):
        self.idade = idade

    def setSaude (self, saude):
        self.saude = saude

    def getNome(self):
        return self.nome
    
    def getFome(self):
        return self.getFome

    def getSaude(self):
        return self.getSaude

    def getIdade(self):
        return self.getIdade

    def Humor(self):
        return self.getFome() * self.getSaude()

    def Alimenta(self, quantidade):
        if quantidade >=0 and quantidade <= 100:
            self.nome -= self.fome * (quantidade /100)

    def Brincar (self, quantidade):
        if quantidade >= 0 and quantidade <= 100:
            self.saude += self.saude * ( quantidade / 100)

    def str(self):
        return (f"Nome: {self.getNome}, Fome: {self.getFome}, saúde: {self.getSaude}, idade: {self.getIdade}")

nome = input("Digite o nome do seu bichinho: ")
idade = int(input("Digite a idade: "))
bicho1 = BichinhoVirtual(nome, random.randint(0,10), random.randint(0,10),idade)
nome1 = input("Digite o noem do bichinho 2: ")
idade1 = int(input("Digite a idade: "))
bicho2 = BichinhoVirtual(nome1, random.randint(0,10), random.randint(0,10),idade1)
nome2 = input("Digite o nome do bicnho 3: ")
idade2 = int(input("Digite a idade: "))
bicho3 = BichinhoVirtual(nome2, random.randint(0,10), random.randint(0,10),idade2)
fazenda = []
fazenda.append(bicho1)
fazenda.append(bicho2)
fazenda.append(bicho3)
print(vars(fazenda))

