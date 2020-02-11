import csv

def lue_csv_tiedostosta_vanhin_henkilö(csv_tiedoston_nimi = None, erotinmerkki = None):

    # jos tiedostonimeä ei ole annettu, kysytään se käyttäjältä
    tiedosto = csv_tiedoston_nimi
    if tiedosto is None:
        tiedosto = input("Anna CSV-tiedoston nimi ja polku: ")

    # jos erotinmerkkiä ei ole annettu, oletetaan sen olevan puolipiste
    if erotinmerkki is None:
        erotinmerkki = ";"
    
    # aloitetaan CSV-tiedoston lukeminen
    suurin_ikä = -9999
    with open(tiedosto) as csvfile:
        lukija = csv.reader(csvfile, delimiter = erotinmerkki)
        for osat in lukija:
            try:
                nimi = osat[0]
                ikä = int(osat[1])
                if (ikä > suurin_ikä):
                    suurin_ikä = ikä
                    vanhin_henkilö = nimi
            except:
                print("Rivin lukemisessa ongelma:", osat)

    print("Vanhin henkilö on", vanhin_henkilö, ", ikä on", suurin_ikä)

try:
    luettava_csv = r"C:\Academy\Oulu\1-2020\Python\Nimet.csv"
    lue_csv_tiedostosta_vanhin_henkilö(luettava_csv)

except FileNotFoundError:
    print("CSV-tiedostoa ei löydy:",luettava_csv)
#except:
    #print("CSV-tiedoston lukeminen ei onnistunut.")

print("Sovelluksen suoritus päättyy.")
