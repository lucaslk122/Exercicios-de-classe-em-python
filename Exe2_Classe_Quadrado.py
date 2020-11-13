"""
Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
    """

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def MudaLado(self,lado):
        self.lado = lado
        

    def Area(self,lado = 0, lado_novo = 0):
        return self.lado * self.lado or lado_novo * lado_novo
        

def main():
    lado = int(input("Digite um valor para o lado do quadrado: "))
    quadrado = Quadrado(lado)
    print(f"Area do quadrado: {quadrado.Area(lado)} m^2")
    troca = input("Dseja trocar o valor do lado? s/n: ").lower()
    if troca == "s":
        lado_novo = int(input("Digite o novo valor: "))
        quadrado.MudaLado(lado_novo)
        print((f"A nova area é {quadrado.Area(lado_novo)} m^2"))
    else:
        print("A area continua a mesma")
    
main()

