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

    def depósito(self, deposito):
        self.saldo += deposito

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor


nome = input("Digite seu nome: ")
numero_conta = int(input("Digite o numero da conta: "))
saldo = int(input("Digite o valor do saldo: "))
conta = ContaCorrente(nome, numero_conta, saldo)
print(vars(conta))
resposta = input("Dseja trocar de nome? s/n: ").lower()
if resposta == "s":
    nome = input("Digite o novo nome: ") 
    conta.alterarNome(nome)
else:
    pass
deposito = float(input("Digite o valor do deposito: "))
conta.depósito(deposito)
saque = float(input("Digite o valor do saque: "))
conta.saque(saque)
print(vars(conta))