"""
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
    """

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def MudaLado(self,lado):
        lado_novo = self.lado
        return lado_novo

    def Area(self,lado = 0, lado_novo = 0):
        return self.lado * self.lado
        

def main():
    lado = int(input("Digite um valor para o lado do quadrado: "))
    quadrado = Quadrado(lado)
    print(f"Area do quadrado: {quadrado.Area(lado)}m^2")
    
main()

