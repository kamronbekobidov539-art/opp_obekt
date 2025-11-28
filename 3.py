class Avto:
    def __init__(self, model, yil, tezlik=0):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def tezlashtir(self):
        self.tezlik += 10

    def sekinlashtir(self):
        self.tezlik -= 10

    def info(self):
        print(f"Model: {self.model}, Yil: {self.yil}, Tezlik: {self.tezlik}")


a = Avto("Malibu", 2022)

a.tezlashtir()
a.tezlashtir()
a.tezlashtir()

a.sekinlashtir()

a.info()
