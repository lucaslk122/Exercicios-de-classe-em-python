"""
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self,ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def Centro(self):
        x_centro = (self.ladoA.x + self.ladoB.x) / 2
        y_centro = (self.ladoA.y + self.ladoB.y) / 2
        return f"X = {x_centro}"
        return f"Y = {y_centro}"

def Main():
    x1 = float(input("Digite a coordenada x do canto inferior esquerdo: "))
    y1 = float(input("Digite a coordenada y do canto inferior esquerdo: "))
    ladoA = Ponto(x1,y1)
    x2 = float(input("Digite a coordenada x do canto superior direito: "))
    y2 = float(input("Digite a coordenada y do canto superior direito: "))
    ladoB = Ponto(x2,y2)
    ret = Retangulo(ladoA, ladoB)
    print(f"Ponto central: {ret.Centro()}")

Main()