class Asiakas:

    testi_attribuutti = 50
    
    def __init__(self, nimi):
        super().__init__()
        self.attribuutti_yksi = 100
        self.attribuutti_kaksi = 200
        self.asiakkaan_nimi = nimi

    def tulosta(self):
        print(self.asiakkaan_nimi, self.attribuutti_yksi, self.attribuutti_kaksi, self.testi_attribuutti)


asiakas1 = Asiakas("Antti Asiakas")
asiakas2 = Asiakas("Teppo Testaaja")
# print(asiakas1)
# print(asiakas2)

asiakas1.tulosta()
asiakas2.tulosta()

# print(asiakas1.testi_attribuutti)
# print(asiakas1.attribuutti_yksi)

# asiakas1.uusi_tieto = 123
# print(asiakas1.uusi_tieto)
# print(asiakas2.uusi_tieto)    <-- ei toimi
