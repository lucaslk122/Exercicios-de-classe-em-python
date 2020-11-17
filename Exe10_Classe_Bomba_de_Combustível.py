"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

class BombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self,valorLitro, quantidadeCombustivel):
        return valorLitro * quantidadeCombustivel

    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarQuantidadeCombustivel(self, valorLitro, quantidadeCombustivel):
        return valorLitro * quantidadeCombustivel
        
tipoCombustivel = input("Qual é o tipo de combustivel: ")
valorLitro = float(input("Qual o valor por litro do combustivel?: "))
quantidadeCombustivel = float(input("Informe a quantidade de combustivel: "))
posto = BombaCombustível(tipoCombustivel, valorLitro, quantidadeCombustivel)
print(f"Valor a ser pago pelo combutivel {tipoCombustivel}: R${posto.abastecerPorValor(valorLitro, quantidadeCombustivel)}")
pergunta = input("Deseja mudar os parametros? s/n: ").lower()
if pergunta == "n":
    pass
else:
    tipoCombustivel = input("Qual será o combustivel?: ")
    valorLitro = float(input("Digite o valor do litro do combustivel: "))
    quantidadeCombustivel = float(input("Informe a quantidade de combustivel: "))
    BombaCombustível.alterarCombustivel(valorLitro, quantidadeCombustivel)
    print(f"Valor a ser pago pelo combutivel {tipoCombustivel}: R${posto.alterarQuantidadeCombustivel(valorLitro, quantidadeCombustivel)}")