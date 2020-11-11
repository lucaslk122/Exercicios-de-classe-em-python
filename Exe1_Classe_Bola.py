"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, cor = "Desconhecido", circunferencia = "Desconhecido", material = "Desconhecido"):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        troca = input("Quer trocar de cor? s/n: ").lower()
        if troca == "s":
            nova_cor = input("Nova cor: ")
        else:
            print("A cor continua a mesma")

    def mostraCor(self):
        print(f"A cor atual é {self.cor}")

def main():
    cor = input("Digite a cor: ")
    circunferencia = int(input("Digite a circunferencia: "))
    material = input("Digite o material: ")
    bola1 = Bola(cor, circunferencia, material)
    while True:
        bola1.mostraCor()
        bola1.trocaCor()
        cont = input("Continuar? s/n: ").lower()
        if cont == "n":
            break
        bola1.mostraCor()
    
main()