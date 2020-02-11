import fileinput

luettava_csv = r"C:\Academy\Oulu\1-2020\Python\Nimet.csv"
suurin_ikä = -9999
vanhin_henkilö = ""

with fileinput.input(files=(luettava_csv)) as f:
    for line in f:
        osat = line.split(";")
        nimi = osat[0]
        ikä = int(osat[1].strip("\n"))
        # print(ikä)
        if (ikä > suurin_ikä):
            suurin_ikä = ikä
            vanhin_henkilö = nimi
            # print("Löytyi vanhin")
        
print("Vanhin henkilö on", vanhin_henkilö, ", ikä on", suurin_ikä)
