class Mahsulot:
    def __init__(self, nom, narx, miqdor):
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor

    def sotib_ol(self, miqdor):
        if miqdor <= self.miqdor:
            self.miqdor -= miqdor
            print(f"{miqdor} ta sotib olindi.")
        else:
            print("Yetarli mahsulot yo‘q!")

    def qolgan_miqdor(self):
        return self.miqdor


# Obyekt
m1 = Mahsulot("Olma", 5000, 20)

m1.sotib_ol(5)
m1.sotib_ol(3)

print("Qolgan:", m1.qolgan_miqdor())
