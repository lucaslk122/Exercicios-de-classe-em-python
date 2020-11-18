"""
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
"""

class Funcionario:

    def __init__(self, nome:str, salario:float):
        self.nome = nome
        self.salario = salario

    def MostraNomeESalario(self, nome, salario):
        print(f"Nome do funcionario: {self.nome}, Salario: R${self.salario}")

    def aumentarSalario (porcentualDeAumento, salario):
         print(f"Novo salario: {salario + (salario * (porcentualDeAumento/100))}")
       

nome = input("Digite seu nome: ")
salario = float(input("Entre com seu salario: "))
funcionario = Funcionario(nome, salario)
funcionario.MostraNomeESalario(nome, salario)
porcentualDeAumento = int(input("Entre com a porcentagem de aumento: "))
Funcionario.aumentarSalario(porcentualDeAumento, salario)