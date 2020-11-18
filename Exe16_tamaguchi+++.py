"""
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.
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
        return self.fome * self.saude

    def Alimento(self, quantidade):
        if (quantidade >= 0 and quantidade <=100):
            self.fome -= self.fome * (quantidade / 100)
        else:
            print("Qunatidade fora do range")

    def Brincar(self, quantidade):
        if (quantidade >= 0 and quantidade <=100):
            self.saude += self.saude*(quantidade /100)
        else:
            print("Seu bichinho não tem saude o suficiente")

nome = input("Digite o nome: ")
fome = int(input("Digite a fome: "))
saude = int(input("Digite a saude: "))
idade = int(input("Digite a idade: "))
bichinho = BichinhoVirtual(nome, fome, saude, idade)
print(f"Humor do seu tamaguchi: {bichinho.Humor()}")
alimentacao = int(input("Quanto deseja alimentar?: "))
bichinho.Alimento(alimentacao)
print(f"Humor do seu tamaguchi: {bichinho.Humor()}")
brincar = int(input("Quanto deseja brincar?: "))
print(f"Humor do seu tamaguchi: {bichinho.Humor()}")