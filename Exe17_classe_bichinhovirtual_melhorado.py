"""
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""

import random

class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.setNome = nome
        self.setfome = fome
        self.setsaude = saude
        self.setIdade = idade 

    def setNome(self, nome):
        self.nome = nome        
        
    def setFome(self, fome):
        self.fome = fome
    
    def setSaude(self, saude):
        self.saude = saude
    
    def setIdade(self, idade):
        self.idade = idade

    def Humor(self):
        return self.setFome() * self.setSaude()

    def Alimenta(self, quantidade):
        if quantidade >=0 and quantidade <= 100:
            self.fome -= self.fome * (quantidade /100)

    def Brincar(self, quantidade):
        if quantidade >= 0 and quantidade <= 100:
            self.saude += self.saude * ( quantidade / 100)

    def String(self):
        return (f"Nome: {self.setNome}, Fome: {self.setFome}, saúde: {self.setSaude}, idade: {self.setIdade}")


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
        alimento = input("Alimentar todos com: ")
        quantidade = int(input("quantidade: "))
        for i in range(3):
            fazenda[i].Alimenta(quantidade)
    elif(op ==2):
        brinquedo = input("Brincar todos com: ")
        quantidade = int(input("quantidade: "))
        for i in range(3):
            fazenda[i].Brincar(quantidade)
    elif(op == 3):
        for i in range(3):
            print(fazenda[i].setNome() + ": " + (fazenda[i].humor()))
    elif(op == 4):
        break
