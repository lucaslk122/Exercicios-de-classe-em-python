"""
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
"""

class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def MudaNome(self, nome):
        self.nome = nome

    def MudaFome(self, fome):
        self.fome = fome

    def MudaSaude(self, saude):
        self.saude = saude
    
    def MudaIdade(self, idade):
        self.idade = idade

    def Humor(self):

