"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
"""

class Funcionario:

    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self.salario = salario

    def MostraNomeESalario(self, nome, salario):
        return f"Nome do funcionario: {self.nome}, Salario: R${self.salario}"

nome = input("Digite seu nome: ")
salario = float(input("Entre com seu salario: "))
funcionario = Funcionario(nome, salario)
print(funcionario.MostraNomeESalario(nome, salario))