from datetime import datetime

class Tiedostoloki:

    tiedosto_nimi = r"C:\Temp\Testiloki Pythonista.txt"

    def kirjoita(self, viesti):

        nyt = datetime.now()

        loki = open(self.tiedosto_nimi, "a", encoding="utf-8")
        loki.write(str(nyt))
        loki.write(": ")
        loki.write(viesti)
        loki.write("\n")
        loki.close()

# testausta
l = Tiedostoloki()
l.kirjoita("Ensimmäinen rivi.")
l.kirjoita("Toinen rivi.")

print("Loppu.")
