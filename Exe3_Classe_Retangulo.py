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

    def Area(self, ladoA,ladoB):
        return ladoA * ladoB

    def Perimetro(self, ladoA,ladoB):
        return 2 * (ladoA + ladoB)

def main():
    ladoA = int(input("Digite um valor para o lado do retangulo: "))
    ladoB = int(input("Digite um valor para o outro lado do retangulo: "))
    retangulo = Retangulo(ladoA,ladoB)
    print(f"Area do retangulo: {retangulo.Area(ladoA,ladoB)} m^2")
    print(f"Perimetro do retangulo: {retangulo.Perimetro(ladoA,ladoB)} m^2")
    """
    troca = input("Dseja trocar o valor do lado? s/n: ").lower()
    if troca == "s":
        lado_novo = int(input("Digite o novo valor: "))
        quadrado.MudaLado(lado_novo)
        print((f"A nova area é {quadrado.Area(lado_novo)} m^2"))
    else:
        print("A area continua a mesma")
    """

main()