"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def canal(self, numero):
        if numero.isdigt():
            num = numero
            if num > 0 and num <= 100:
                self.canal = num
        else:
            print("Canal deve ser apenas numeros")

    def volume(self, numero):
        if numero.isdigt():
            num = numero
            if num >= 0 and num <= 100:
                self.volume = num
            else:
                print("O volume de ser entra 0 e 100")
        else:
            print("O volume de ser apenas numeros")

canal = int(input("Digite o canal: "))
volume = int(input("Digite o volume: "))
televisão = TV(canal,volume)