"""
Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo():
    def __init__(self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def Area(self, ladoA = 0, ladoB = 0, lado_novoA = 0, lado_novoB = 0):
        return ladoA * ladoB or lado_novoA * lado_novoB

    def Perimetro(self, ladoA = 0, ladoB = 0, lado_novoA = 0, lado_novoB = 0):
        return 2 * (ladoA + ladoB) or 2 * (lado_novoA + lado_novoB)

    def MudaLado(self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

def main():
    ladoA = int(input("Digite um valor para o lado do retangulo: "))
    ladoB = int(input("Digite um valor para o outro lado do retangulo: "))
    retangulo = Retangulo(ladoA,ladoB)
    print(f"Area do retangulo: {retangulo.Area(ladoA,ladoB)} m^2")
    print(f"Perimetro do retangulo: {retangulo.Perimetro(ladoA,ladoB)} m^2")
    troca = input("Dseja trocar o valor dos lados? s/n: ").lower()
    if troca == "s":
        lado_novoA = int(input("Digite o novo valor: "))
        lado_novoB = int(input("Digite o novo valor: "))
        retangulo.MudaLado(lado_novoA, lado_novoB)
        print((f"A nova area é {retangulo.Area(lado_novoA, lado_novoB,)} m^2"))
        print((f"O nova perimetro é {retangulo.Perimetro(lado_novoA, lado_novoB,)} m"))
    else:
        print("A area e o perimetro continuam os mesmos")


main()