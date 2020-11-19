"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""

import random

class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setfome(fome)
        self.setsaude(saude)
        self.setIdade(idade)

    def setNome(self, nome):
        self.nome = nome        
        
    def setFome(self, fome):
        self.fome = fome
    
    def setSaude(self, saude):
        self.saude = saude
    
    def setIdade(self, idade):
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def getFome(self):
        return self.fome
    
    def getSaude(self):
        return self.saude
    
    def getIdade(self):
        return self.idade

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


bicho1 = BichinhoVirtual("lucas", random.randint(0,10), random.randint(0,10),25)
bicho2 = BichinhoVirtual("Sarah", random.randint(0,10), random.randint(0,10),8)
bicho3 = BichinhoVirtual("Pedro", random.randint(0,10), random.randint(0,10),9)
fazenda = []
fazenda.append(bicho1)
fazenda.append(bicho2)
fazenda.append(bicho3)

while True:
    print("-"*20 + "Fazenda" + "-"*20)
    print("1. Alimentar todos os bichos")
    print("2. Brincar com todos os bichos")
    print("3. Ouvir todos os bichos")
    print("4. Sair")
    op = int(input("Digite a opção: "))
    
    if (op == 1):
        alimento = int(input("Alimentar todos com: "))
        for i in range(3):
            fazenda[i].alimenta(alimento)
    elif(op ==2):
        brinquedo = int(input("Brincar todos com: "))
        for i in range(3):
            fazenda[i].brincar(brinquedo)
    elif(op == 3):
        for i in range(3):
            print(fazenda[i].getNome() + ": " + str(fazenda[i].humor()))
    elif(op == 4):
        break

