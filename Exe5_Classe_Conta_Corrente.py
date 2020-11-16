"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

class ContaCorrente:

   def __init__(self, nome,numero_conta, saldo = 0):
        self.nome = nome
        self.saldo = saldo
        self.numero_conta = numero_conta
        
    def alterarNome(self, nome):
        self.nome = nome

    def depósito(self, valor):
        self.saldo = self,valor + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor

nome = input("Digite seu nome: ")
numero_conta = int(input("Digite o numero da conta: "))
saldo = float(input("Digite o saldo: "))
deposito = float(input("Digite o valor do deposito: "))
conta = ContaCorrente(nome,saldo, numero_conta,deposito)
resposta = int("Dseja trocar de nome? s/n: ").lower()
if resposta == "s":
    novo_nome = input("Digite o novo nome: ") 
    conta.alterarNome(novo_nome)
else:
    pass
print()