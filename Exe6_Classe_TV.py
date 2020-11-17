"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class TV:
    def __init__(self):
        self.Canal(0)
        self.volume = 0

    def Canal(self, canal):
        if canal > 0 and canal <= 100:
            self.canal = canal

    def Aumentavolume(self):
        if self.volume < 100:
            self.volume += 1

    def DiminuiVolume (self):
        if self.volume > 0 :
            self.volume += 1

televisao = TV()
canal = int(input("Digite o canal: "))
televisao.Canal(canal)
print(vars(televisao))
#aumentaVolume = int(input("Aumente o volume: "))
televisao.Aumentavolume()
print(vars(televisao))
#diminuivolume = int(input("Diminua o volume: "))
televisao.DiminuiVolume()
print(vars(televisao))
