class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def qidirish(self, nom):
        for k in self.kitoblar:
            if k.nomi == nom:
                return f"Topildi: {k.nomi} — {k.muallif}"
        return "Topilmadi!"


# Kutubxona obyektini yaratish
k = Kutubxona()

k.kitob_qoshish(Kitob("O'tkan kunlar", "O'.H"))
k.kitob_qoshish(Kitob("Sariq devni minib", "X.To'xtaboyev"))
k.kitob_qoshish(Kitob("Shum bola", "G'.Gulom"))

print(k.qidirish("Shum bola"))
