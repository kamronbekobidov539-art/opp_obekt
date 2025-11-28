class Kurs:
    def __init__(self, nomi, davomiylik):
        self.nomi = nomi
        self.davomiylik = davomiylik
        self.talabalar = []

    def talaba_qoshish(self, ism):
        self.talabalar.append(ism)

    def talabalar_soni(self):
        return len(self.talabalar)


k1 = Kurs("Python", 6)

k1.talaba_qoshish("Ali")
k1.talaba_qoshish("Vali")
k1.talaba_qoshish("Sami")

print(k1.talabalar_soni())
